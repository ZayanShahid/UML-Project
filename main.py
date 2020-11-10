from demo_db import DemoDB
from batch import Batch


if __name__ == "__main__":
    
    db = DemoDB()
    db.existing_records()

    records_res = db.display_all_records()

    # print(records_res)

    new_batch = Batch()  
    new_batch.b_id = input("Enter Batch Id: ")
    new_batch.teacher.fullAddress.city = input("Enter City Name")

    db.add_new_batch(new_batch)

