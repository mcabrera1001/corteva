from config.flask_and_database import db, app
import logging
import os


def add_object_to_db(model_object):
    with app.app_context():
        db.session.add(model_object)
        db.session.commit()


def process_ingestion_results(ingestion_results):
    ingested_amount = len([result for result in ingestion_results if not result])
    logging.info(
        f"Successfully ingested a total of {ingested_amount} out of {len(ingestion_results)} records."
    )


def generate_list_of_files(directory):
    data_files = os.listdir(directory)
    return data_files



