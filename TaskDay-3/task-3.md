## Task Day-3


1. Create environment 

* pilih composer sesuai kebutuhan. Composer 1 menyediakan Airflow 1 & 2, sedangkan Composer 2 hanya Airflow 2 namun bisa Autoscaling.

* Disini saya menggunakan composer 2.

![composer](screenshot/1.CreateComposer.png)

2. Kemudian Lakukan Configuration lalu Klik Create

![fill](screenshot/2.configuration.PNG)


3. Tunggu hingga proses selesai

![wait](screenshot/3.wait-processing.PNG)

* Setelah proses selesai, environment berhasil dibuat

![created](screenshot/4.Finish-process.PNG)

4. Upload DAG dengan menjalankan script berikut:
```
gcloud composer environments storage dags import \
    --environment my-environment \
    --location asia-southeast1 \
    --source="cloud-composer/insert.py"
```

![uploading](screenshot/5.script-uploadDAG.PNG)

* DAG sudah diupload
![uploading](screenshot/6.UploadDAGonAirflowUI.PNG)

    ![uploading](screenshot/6.UploadDAGonBucket.PNG)

    ![uploading](screenshot/6.UploadDAG.PNG)


5. Pengecekan Data di BigQuery

Data sudah berhasil di insert ke my_table

![inserted](screenshot/7.Result.PNG)

* DAG yang sudah berhasil diupload bisa ditrigger dan dipause secara manual di UI Airflow

    ![uploading](screenshot/6.TriggerDAG.PNG)



6. Delete DAG
```
gcloud composer environments storage dags delete \
    --environment my-environment \
    --location asia-southeast1 \
    cloud-composer/insert.py
```


![y_delete](screenshot/8.DeleteDAG.PNG)

* DAG berhasil dihapus

    ![y_delete](screenshot/8.DeleteDAGonComposer.PNG)

    ![y_delete](screenshot/8.DeleteDAGonAirflow.PNG)
