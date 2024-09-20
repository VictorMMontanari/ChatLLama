from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    {
        "Code": 1,
        "name": "Panic disorder",
        "symptoms": "Palpitations, Sweating, Trembling, Shortness of breath, Fear of losing control, Dizziness",
        "treatments": "Antidepressant medications, Cognitive Behavioral Therapy, Relaxation Techniques"
    },
    {
        "Code": 2,
        "name": "Vocal cord polyp",
        "symptoms": "Hoarseness, Vocal Changes, Vocal Fatigue",
        "treatments": "Voice Rest, Speech Therapy, Surgical Removal"
    },
    {
        "Code": 3,
        "name": "Turner syndrome",
        "symptoms": "Short stature, Gonadal dysgenesis, Webbed neck, Lymphedema",
        "treatments": "Growth hormone therapy, Estrogen replacement therapy, Cardiac and renal evaluations"
    },
    {
        "Code": 4,
        "name": "Cryptorchidism",
        "symptoms": "Absence or undescended testicle(s), empty scrotum, smaller or underdeveloped testicle(s), inguinal hernia, abnormal positioning of the testicle(s) (higher in the groin area)",
        "treatments": "Observation and monitoring (in cases of mild or transient cryptorchidism), hormone therapy (to stimulate testicular descent), surgical intervention (orchiopexy) to reposition the testicle(s) into the scrotum, if necessary, performed around the age of 6 to 12 months, open or laparoscopic surgery (in cases of high or persistent cryptorchidism), testicular prostheses (in cases of absent or non-functional testicles), regular follow-up visits with a urologist or pediatric surgeon"
    }
]

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="my_books",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)

client.upload_points(
    collection_name="my_books",
    points=[
        models.PointStruct(
            id=idx, vector=encoder.encode(doc["symptoms"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)