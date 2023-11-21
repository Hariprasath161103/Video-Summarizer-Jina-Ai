import http.client
import json
import os
import time

YOUR_GENERATED_SECRET = "y6WkIIEp7v6iopPO34sv:8b43ac4fc4766e0831d1111255e734e68f15ec4bdcd8182d1674e49cf227f8ce"

data = {
    "data": [
        {
            "video": "https://firebasestorage.googleapis.com/v0/b/causal-diffusion.appspot.com/o/uploads%2Fchunks%2FMGUqOXfMlNOBkJvh6kqrA4j4t2C2%2F1700508474112%2Fvenky.mp4?alt=media&token=046a2337-7fed-475f-a724-d5002152552a",
            "algorithm": "Inception",
            "languages": ["en"]
        }
    ]
}

headers = {
    "x-api-key": f"token {YOUR_GENERATED_SECRET}",
    "content-type": "application/json",
}



with open('output3.txt', 'w') as f:
    pass

connection = http.client.HTTPSConnection("api.scenex.jina.ai")
connection.request("POST", "/v1/describe", json.dumps(data), headers)
response = connection.getresponse()


response_data = response.read().decode("utf-8")


with open('output.txt', 'a') as f:
    f.writelines(response_data)


f.close()
print("Summarizing...")

#print("The response file is succesfully saved.")


task_id = json.loads(response_data).get("result", [])[0].get("id", "")


while True:
    
    connection = http.client.HTTPSConnection("api.scenex.jina.ai")
    connection.request("GET", f"/v1/task/{task_id}", headers=headers)
    response = connection.getresponse()


    response_data = response.read().decode("utf-8")

    print(response_data)

    try:
     
        status = json.loads(response_data).get("status", "")

        if status != "pending":
            print("The response file is succesfully saved.")
            break  # Exit the loop if the status is not "pending"

    except json.decoder.JSONDecodeError:
        
        print("Pending")

    connection.close()


connection.close()
