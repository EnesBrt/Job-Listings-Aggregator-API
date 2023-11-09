from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from test_scraping import scraping
from data import data_preprocessing, database_insertion
from selenium import webdriver


app = Flask(__name__)

# connetion à la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://enesbarut:barut_admin@localhost:5432/jobscraping'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class JobListing(db.Model):
    # model de la base de données qui représente la table joblistings
    __tablename__ = 'job_listings'
    
    job_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(255))
    company_name = db.Column(db.String(255))
    job_type = db.Column(db.String(255))
    
    def to_dict(self):
        return {
            'job_id': self.job_id,
            'title': self.title,
            'location': self.location,
            'company_name': self.company_name,
            'job_type': self.job_type
        }
        
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Real-time Job Listings Aggregator API"})
        

    @app.route('/scraping_jobs', methods=['GET'])
    def scrap_all_jobs():
        try:
            driver = webdriver.Safari()
            driver.implicitly_wait(10)
            base_url = 'https://www.welcometothejungle.com/fr/jobs?query=python&refinementList%5Boffices.country_code%5D%5B%5D=FR&page='
            jobs = scraping(driver, base_url)  # Passez l'instance de driver et base_url
            driver.quit()  # Assurez-vous de fermer le driver après l'utilisation
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        # Traitement des données et insertion dans la base de données
        df = data_preprocessing()
        database_insertion(df)
        return jsonify({"message": "Scraping done and data inserted successfully into the database"})

    
    @app.route('/jobs', methods=['GET'])
    def get_jobs():
        jobs = JobListing.query.all()
        return jsonify([job.to_dict() for job in jobs])
    
    @app.route('/jobs_post', methods=['POST'])
    
    def create_job():
        data = request.get_json()
        new_job = JobListing(
            title=data['title'], 
            location=data['location'], 
            company_name=data['company_name'], 
            job_type=data['job_type']
        )
        db.session.add(new_job)
        db.session.commit()
        return jsonify(new_job.to_dict()), 201

    
    @app.route('/jobs/<int:job_id>', methods=['PUT'])
    def update_job(job_id):
        job = JobListing.query.get_or_404(job_id)
        data = request.get_json()
        job.title = data['title']
        job.location = data['location']
        job.company_name = data['company_name']
        job.job_type = data['job_type']
        db.session.commit()
        return jsonify(job.to_dict())
    
    @app.route('/jobs/<int:job_id>', methods=['DELETE'])
    def delete_job(job_id):
        job = JobListing.query.get_or_404(job_id)
        db.session.delete(job)
        db.session.commit()
        return jsonify({'message': 'Job deleted'}), 200
    
    @app.route('/jobs', methods=['DELETE'])
    def delete_all_jobs():
        db.session.query(JobListing).delete()
        db.session.commit()
        return jsonify({'message': 'All jobs deleted'}), 200
        

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
    