from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv()
urlQdrant=os.getenv('DATABASE_URL')
apiQdrant=os.getenv('CHAVE_QDRANT')

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
    },
    {
        "Code": 5,
        "name": "Ethylene glycol poisoning-1",
        "symptoms": "Nausea, vomiting, abdominal pain, General malaise, weakness, Increased thirst, frequent urination",
        "treatments": "Supportive Measures, Gastric Decontamination, Antidote Administration, Hemodialysis"
    },
    {
        "Code": 6,
        "name": "Ethylene glycol poisoning-2",
        "symptoms": "Metabolic acidosis, apid breathing, rapid heart rate, confusion, headache, dizziness, seizures",
        "treatments": "Blood tests, Supportive Measures, Gastric Decontamination, Antidote Administration, Hemodialysis"
    },
    {
        "Code": 7,
        "name": "Ethylene glycol poisoning-3",
        "symptoms": "Decreased urine output, swelling in the legs and ankles, and signs of fluid overload, Severe kidney damage",
        "treatments": "Supportive Measures, Gastric Decontamination, Antidote Administration, Hemodialysis"
    },
    {
        "Code": 8,
        "name": "Atrophic vaginitis",
        "symptoms": "Vaginal dryness, Vaginal burning, frequent urination, urinary tract infections, Painful intercourse",
        "treatments": "Vaginal moisturizers, Vaginal estrogen therapy, Lifestyle modifications"
    },
    {
        "Code": 9,
        "name": "Fracture",
        "symptoms": "Pain, Swelling, Bruising, Deformity, Difficulty moving, Loss of function",
        "treatments": "Immobilization, Surgery, Rehabilitation"
    },
    {
        "Code": 10,
        "name": "Cellulitis",
        "symptoms": "Redness, Pain, tenderness, Swelling, Skin changes, Lymph node enlargement",
        "treatments": "Antibiotics, Warm compresses, immobilization, rest, Pain management"
    },
    {
        "Code": 11,
        "name": "Eye alignment disorder",
        "symptoms": "Double vision, Eye fatigue, Poor depth perception, Head tilting",
        "treatments": "Glasses, Patching therapy, Vision therapy, Botox injections, Surgical intervention"
    },
    {
        "Code": 12,
        "name": "Headache after lumbar puncture",
        "symptoms": "throbbing headache",
        "treatments": "Epidural blood patch, Conservative measures"
    },
    {
        "Code": 13,
        "name": "Pyloric stenosis",
        "symptoms": "Persistent hunger, Weight loss, Dehydration, Visible peristalsis, Palpable mass, Fussiness ",
        "treatments": "Ultrasound, Blood tests, Pyloromyotomy"
    },
    {
        "Code": 14,
        "name": "Adenoid cystic carcinoma",
        "symptoms": "Lump, swelling, Facial numbness, tingling",
        "treatments": "Surgery, Radiation therapy"
    },
    {
        "Code": 15,
        "name": "Pleomorphic adenoma",
        "symptoms": "Painless lump or swelling, Facial changes",
        "treatments": "Surgical excision"
    },
    {
        "Code": 16,
        "name": "Warthin tumor",
        "symptoms": "Painless lump or swelling, Facial changes",
        "treatments": "Surgical excision"
    },
    {
        "Code": 17,
        "name": "Mucoepidermoid carcinoma",
        "symptoms": "Lump, swelling, Difficulty, pain when swallowing and speaking, Facial weakness, Facial paralysis ",
        "treatments": "Surgery, Radiation therapy"
    },
    {
        "Code": 18,
        "name": "Acinic cell carcinoma",
        "symptoms": "Lump, swelling, Facial changes",
        "treatments": "Surgery, Radiation therapy"
    },
    {
        "Code": 19,
        "name": "Mucocele",
        "symptoms": "Painless fluid-filled swelling in the oral cavity",
        "treatments": "Observation, Surgical removal if necessary"
    },
    {
        "Code": 20,
        "name": "Osteochondrosis",
        "symptoms": "Joint pain, stiffness, swelling, reduced range of motion",
        "treatments": "Physical therapy, pain medications, rest, surgery"
    },
    {
        "Code": 21,
        "name": "Sialolithiasis",
        "symptoms": "Swelling, pain, tenderness, difficulty eating",
        "treatments": "Warm compresses, Saliva stimulation, Sialagogues, Stone removal "
    },
    {
        "Code": 22,
        "name": "Submandibular stones",
        "symptoms": "Swelling, pain, dry mouth, bad taste",
        "treatments": "Hydration,Saliva stimulation, Stone removal"
    },
    {
        "Code": 23,
        "name": "Parotid stones",
        "symptoms": "Swelling, pain, dry mouth, bad taste",
        "treatments": "Hydration,Saliva stimulation, Stone removal"
    },
    {
        "Code": 24,
        "name": "Recurrent salivary stones",
        "symptoms": "Frequent episodes of stone formation",
        "treatments": "Hydration,Saliva stimulation, Stone removal"
    },
    {
        "Code": 25,
        "name": "Wharton's duct stones",
        "symptoms": "Swelling, pain, dry mouth, bad taste",
        "treatments": "Hydration,Saliva stimulation, Stone removal"
    },
    {
        "Code": 26,
        "name": "Mumps",
        "symptoms": "Swollen salivary glands (usually parotid), fever, headache, fatigue",
        "treatments": "Supportive care, pain relievers, isolation, vaccination (MMR)"
    },
    {
        "Code": 27,
        "name": "Ludwig's angina",
        "symptoms": "Severe swelling of the floor of the mouth, fever, difficulty swallowing, drooling",
        "treatments": "Intravenous antibiotics, airway management, surgical drainage"
    },
    {
        "Code": 28,
        "name": "Mucocele",
        "symptoms": "Painless swelling, usually on the lower lip or floor of the mouth",
        "treatments": "Observation, surgical removal if necessary"
    },
    {
        "Code": 29,
        "name": "Abscess",
        "symptoms": "Swelling, pain, redness, fever, pus formation",
        "treatments": "Antibiotics, surgical drainage"
    },
    {
        "Code": 30,
        "name": "Sjögren's syndrome",
        "symptoms": "Dry mouth and eyes, fatigue, joint pain, dry skin",
        "treatments": "Symptomatic relief with artificial tears, saliva substitutes, frequent sips of water, medications to stimulate saliva production, immune-modulating drugs"
    },
    {
        "Code": 31,
        "name": "Open-Angle Glaucoma",
        "symptoms": "Gradual loss of peripheral vision, tunnel vision",
        "treatments": "Eye drops to lower intraocular pressure (e.g., prostaglandin analogs, beta blockers, alpha agonists, carbonic anhydrase inhibitors), oral medications (e.g., carbonic anhydrase inhibitors), laser trabeculoplasty, surgical procedures (e.g., trabeculectomy, glaucoma drainage implants)"
    },
    {
        "Code": 32,
        "name": "Angle-Closure Glaucoma",
        "symptoms": "Severe eye pain, headache, blurred vision, halos around lights, nausea and vomiting",
        "treatments": "Medications (e.g., oral or intravenous acetazolamide, topical beta blockers, alpha agonists, prostaglandin analogs), laser peripheral iridotomy, surgical procedures (e.g., trabeculectomy, glaucoma drainage implants)"
    },
    {
        "Code": 33,
        "name": "Normal-Tension Glaucoma",
        "symptoms": "Gradual loss of vision, visual field defects",
        "treatments": "Eye drops to lower intraocular pressure (e.g., prostaglandin analogs, beta blockers, alpha agonists, carbonic anhydrase inhibitors), oral medications (e.g., carbonic anhydrase inhibitors), laser trabeculoplasty, surgical procedures (e.g., trabeculectomy, glaucoma drainage implants)"
    },
    {
        "Code": 34,
        "name": "Congenital Glaucoma",
        "symptoms": "Cloudy or hazy eyes, excessive tearing, sensitivity to light",
        "treatments": "Surgery (e.g., trabeculotomy, goniotomy) to create a new drainage pathway, medications to reduce intraocular pressure"
    },
    {
        "Code": 35,
        "name": "Secondary Glaucoma",
        "symptoms": "Varies depending on the underlying cause",
        "treatments": "Treatment of the underlying condition (e.g., medication adjustments, surgery, trauma management, tumor removal, inflammation control)"
    },
    {
        "Code": 36,
        "name": "Pigmentary Glaucoma",
        "symptoms": "Blurred vision, halos around lights, eye pain",
        "treatments": "Eye drops to lower intraocular pressure (e.g., prostaglandin analogs, beta blockers, alpha agonists, carbonic anhydrase inhibitors), laser trabeculoplasty, surgical procedures (e.g., trabeculectomy, glaucoma drainage implants)"
    },
    {
        "Code": 37,
        "name": "Exfoliation Glaucoma",
        "symptoms": "Elevated intraocular pressure, visual field loss",
        "treatments": "Eye drops to lower intraocular pressure (e.g., prostaglandin analogs, beta blockers, alpha agonists, carbonic anhydrase inhibitors), laser trabeculoplasty, surgical procedures (e.g., trabeculectomy, glaucoma drainage implants)"
    },
    {
        "Code": 38,
        "name": "Ocular Hypertension",
        "symptoms": "Elevated intraocular pressure without optic nerve damage",
        "treatments": "Observation with regular eye exams, use of eye drops to lower intraocular pressure (if necessary)"
    },
    {
        "Code": 39,
        "name": "Low-Tension Glaucoma",
        "symptoms": "Gradual loss of vision, visual field defects",
        "treatments": "Eye drops to lower intraocular pressure (e.g., prostaglandin analogs, beta blockers, alpha agonists, carbonic anhydrase inhibitors), oral medications (e.g., carbonic anhydrase inhibitors), laser trabeculoplasty, surgical procedures (e.g., trabeculectomy, glaucoma drainage implants)"
    },
    {
        "Code": 40,
        "name": "Anorexia Nervosa",
        "symptoms": "Extreme weight loss, fear of gaining weight, distorted body image",
        "treatments": "Medical monitoring, nutritional counseling, psychotherapy (such as cognitive-behavioral therapy or family-based therapy), medications (in some cases), hospitalization (for severe cases), support groups"
    },
    {
        "Code": 41,
        "name": "Bulimia Nervosa",
        "symptoms": "Recurrent episodes of binge eating followed by purging behaviors",
        "treatments": "Psychotherapy (such as cognitive-behavioral therapy or dialectical behavior therapy), nutritional counseling, medications (in some cases), support groups"
    },
    {
        "Code": 42,
        "name": "Binge Eating Disorder",
        "symptoms": "Recurrent episodes of binge eating without compensatory behaviors",
        "treatments": "Psychotherapy (such as cognitive-behavioral therapy or interpersonal therapy), nutritional counseling, medications (in some cases), support groups"
    },
    {
        "Code": 43,
        "name": "Avoidant/Restrictive Food Intake Disorder (ARFID)",
        "symptoms": "Avoidance or restriction of certain foods or entire food groups, significant weight loss or failure to gain weight",
        "treatments": "Nutritional counseling, psychotherapy (such as cognitive-behavioral therapy or family-based therapy), medical monitoring, exposure therapy, occupational therapy"
    },
    {
        "Code": 44,
        "name": "Other Specified Feeding or Eating Disorder (OSFED)",
        "symptoms": "Symptoms that do not meet the full criteria for a specific eating disorder",
        "treatments": "Treatment is based on the specific symptoms and can include a combination of psychotherapy, nutritional counseling, medical monitoring, and medications as necessary"
    },
    {
        "Code": 45,
        "name": "Orthorexia Nervosa",
        "symptoms": "Obsessive focus on 'clean' eating, healthy food choices",
        "treatments": "Psychotherapy (such as cognitive-behavioral therapy or acceptance and commitment therapy), nutrition education, challenging distorted beliefs, addressing underlying issues"
    },
    {
        "Code": 46,
        "name": "Pica",
        "symptoms": "Persistent consumption of non-food substances",
        "treatments": "Behavioral therapy, addressing underlying nutritional deficiencies, addressing any medical complications, family support"
    },
    {
        "Code": 47,
        "name": "Rumination Disorder",
        "symptoms": "Repeated regurgitation and re-chewing of food",
        "treatments": "Behavioral therapy (such as diaphragmatic breathing techniques), biofeedback, addressing any underlying psychological or medical conditions, dietary modifications"
    },
    {
        "Code": 48,
        "name": "Transient ischemic attack",
        "symptoms": "Sudden onset of neurological symptoms that resolve within 24 hours",
        "treatments": "Antiplatelet medications, Carotid endarterectomy,  Anticoagulant medications, Lifestyle modifications"
    },
    {
        "Code": 49,
        "name": "Pyelonephritis",
        "symptoms": "Fever, chills, back or flank pain, frequent urination",
        "treatments": "Antibiotics (such as fluoroquinolones, cephalosporins, or trimethoprim-sulfamethoxazole) to target the specific bacteria causing the infection, adequate hydration, pain management (such as over-the-counter pain relievers or prescription medications), hospitalization (for severe cases or complications), urine culture to guide antibiotic therapy"
    },
    {
        "Code": 50,
        "name": "Rotator Cuff Injury",
        "symptoms": "Shoulder pain, weakness or loss of strength, limited range of motion, shoulder stiffness",
        "treatments": "Non-surgical treatment options: Rest, ice or heat therapy, pain medications, physical therapy exercises, Arthroscopic surgery"
    },
    {
        "Code": 51,
        "name": "Fibromyalgia",
        "symptoms": "Widespread musculoskeletal pain, fatigue, sleep disturbances",
        "treatments": "Medications (such as pain relievers, antidepressants, anticonvulsants), physical therapy, cognitive-behavioral therapy, stress management techniques, exercise, relaxation techniques, good sleep hygiene"
    },
    {
        "Code": 52,
        "name": "Chronic Fatigue Syndrome",
        "symptoms": "Extreme fatigue, cognitive difficulties, unrefreshing sleep",
        "treatments": "Symptom management (such as medications to address pain, sleep disturbances, and other symptoms), graded exercise therapy, cognitive-behavioral therapy, sleep management techniques, pacing and energy conservation, stress reduction techniques, nutritional support, medications for specific symptoms"
    },
    {
        "Code": 53,
        "name": "Complex Regional Pain Syndrome (CRPS)",
        "symptoms": "Severe and persistent pain, changes in skin color or temperature, swelling, stiffness",
        "treatments": "Medications (such as pain relievers, corticosteroids, anticonvulsants), physical therapy, sympathetic nerve blocks, spinal cord stimulation, occupational therapy, mirror therapy, psychotherapy, graded motor imagery, stress management techniques"
    },
    {
        "Code": 54,
        "name": "Myofascial Pain Syndrome",
        "symptoms": "Localized muscle pain, trigger points",
        "treatments": "Physical therapy, trigger point injections, dry needling, medications (such as pain relievers, muscle relaxants), relaxation techniques, stress management, massage therapy, myofascial release, heat or cold therapy"
    },
    {
        "Code": 55,
        "name": "Chronic Migraine",
        "symptoms": "Recurrent, disabling migraines",
        "treatments": "Medications (such as preventive medications, pain relievers, triptans), lifestyle modifications (such as identifying triggers, stress management, regular sleep patterns), relaxation techniques, biofeedback, cognitive-behavioral therapy, nerve blocks, Botox injections, neuromodulation devices, acupuncture"
    },
    {
        "Code": 56,
        "name": "Neuropathic Pain",
        "symptoms": "Shooting or burning pain, tingling or numbness",
        "treatments": "Medications (such as antidepressants, anticonvulsants, topical treatments), nerve blocks, spinal cord stimulation, physical therapy, occupational therapy, transcutaneous electrical nerve stimulation (TENS), acupuncture, cognitive-behavioral therapy, relaxation techniques"
    },
    {
        "Code": 57,
        "name": "Gestational Diabetes",
        "symptoms": "High blood sugar levels during pregnancy",
        "treatments": "Blood sugar monitoring, healthy diet modifications, regular exercise, insulin injections (if needed), close monitoring by healthcare provider"
    },
    {
        "Code": 58,
        "name": "Pregnancy-Induced Hypertension",
        "symptoms": "High blood pressure during pregnancy",
        "treatments": "Monitoring blood pressure, lifestyle modifications (such as salt restriction, regular exercise), medication (such as antihypertensive drugs) if necessary, close monitoring by healthcare provider"
    },
    {
        "Code": 59,
        "name": "Gestational Hypertension",
        "symptoms": "High blood pressure without proteinuria (preeclampsia)",
        "treatments": "Monitoring blood pressure, lifestyle modifications (such as salt restriction, regular exercise), medication (such as antihypertensive drugs) if necessary, close monitoring by healthcare provider"
    },
    {
        "Code": 60,
        "name": "Preeclampsia",
        "symptoms": "High blood pressure, proteinuria, swelling, headaches, visual disturbances",
        "treatments": "Bed rest, blood pressure monitoring, frequent prenatal visits, medication (such as antihypertensive drugs), magnesium sulfate (for severe cases), delivery of the baby (in severe cases)"
    },
    {
        "Code": 61,
        "name": "Hyperemesis Gravidarum",
        "symptoms": "Severe nausea and vomiting during pregnancy",
        "treatments": "Intravenous fluids to prevent dehydration, anti-nausea medications, nutritional support, rest, monitoring for weight loss and electrolyte imbalance"
    },
    {
        "Code": 62,
        "name": "Urinary Tract Infection (UTI)",
        "symptoms": "Painful urination, frequent urination, pelvic pain, cloudy urine",
        "treatments": "Antibiotics safe for pregnancy, increased fluid intake, maintaining good hygiene, urine culture and sensitivity testing to guide antibiotic selection"
    },
    {
        "Code": 63,
        "name": "Anemia",
        "symptoms": "Fatigue, weakness, pale skin, shortness of breath",
        "treatments": "Iron supplementation, dietary changes (iron-rich foods), managing underlying causes (such as treating iron deficiency or vitamin B12 deficiency), prenatal vitamins"
    },
    {
        "Code": 64,
        "name": "Pregnancy-Related Back Pain",
        "symptoms": "Lower back pain, discomfort in the pelvic area",
        "treatments": "Prenatal exercises (such as stretching and strengthening exercises), good posture, heat or cold therapy, prenatal massages, supportive devices (such as pregnancy belts), physical therapy"
    },
    {
        "Code": 65,
        "name": "Round Ligament Pain",
        "symptoms": "Sharp or aching pain in the lower abdomen or groin",
        "treatments": "Resting, changing positions slowly, warm compresses, gentle stretching, avoiding sudden movements"
    },
    {
        "Code": 66,
        "name": "Placenta Previa",
        "symptoms": "Vaginal bleeding, painless bleeding in the third trimester",
        "treatments": "Bed rest, avoiding strenuous activity, frequent prenatal check-ups, potential hospitalization, potential cesarean delivery"
    },
    {
        "Code": 67,
        "name": "Carpal Tunnel Syndrome",
        "symptoms": "Tingling, numbness, and pain in the hand and fingers",
        "treatments": "Wrist splints, avoiding repetitive hand movements, applying cold or hot compresses, gentle exercises, ergonomic adjustments"
    },
    {
        "Code": 68,
        "name": "Sciatica",
        "symptoms": "Sharp pain, tingling, or numbness that radiates from the lower back through the hips and down the leg",
        "treatments": "Rest, gentle stretching exercises, warm or cold compresses, prenatal massages, maintaining good posture, avoiding activities that worsen the pain"
    },
    {
        "Code": 69,
        "name": "Varicose Veins",
        "symptoms": "Enlarged, swollen veins, often in the legs",
        "treatments": "Elevating legs, wearing compression stockings, regular exercise, avoiding prolonged sitting or standing, maintaining a healthy weight"
    },
    {
        "Code": 70,
        "name": "Hemorrhoids",
        "symptoms": "Swollen, itchy, or painful veins in the rectal area",
        "treatments": "Increasing fiber intake, staying hydrated, avoiding straining during bowel movements, warm sitz baths, topical creams or ointments, over-the-counter pain relievers (after consulting with a healthcare provider)"
    },
    {
        "Code": 71,
        "name": "Gestational Cholestasis",
        "symptoms": "Itchy skin, particularly on the hands and feet",
        "treatments": ""
    },
    {
        "Code": 72,
        "name": "Liver Cancer",
        "symptoms": "Abdominal pain, jaundice (yellowing of the skin and eyes), unexplained weight loss, loss of appetite, fatigue, nausea, vomiting",
        "treatments": "Surgery, Radiation therapy, Chemotherapy, Targeted therapy, Immunotherapy, Radiofrequency ablation, Transarterial chemoembolization (TACE), Selective internal radiation therapy (SIRT), Palliative care, Clinical trials"
    },
    {
        "Code": 73,
        "name": "Atelectasis",
        "symptoms": "Difficulty breathing, rapid breathing, chest pain",
        "treatments": "Treatment of the underlying cause (such as removal of airway obstruction, treatment of lung infection), deep breathing exercises, coughing techniques, incentive spirometry, chest physiotherapy, bronchodilator medications, supplemental oxygen therapy"
    },
    {
        "Code": 74,
        "name": "Ectopic Pregnancy",
        "symptoms": "Vaginal bleeding, abdominal pain or cramping, shoulder pain (if the fallopian tube ruptures)",
        "treatments": "Immediate medical attention, potential medical procedures (such as medication or surgery to remove the ectopic pregnancy), close monitoring, emotional support"
    },
    {
        "Code": 75,
        "name": "Choledocholithiasis",
        "symptoms": "Abdominal pain (often in the upper right quadrant), jaundice, dark urine, pale stools, nausea, vomiting, endoscopic retrograde cholangiopancreatography (ERCP) with stone removal, sphincterotomy, Cholecystectomy ",
        "treatments": "Non-surgical treatment options: Medications to manage pain and discomfort, antibiotics"
    },
    {
        "Code": 76,
        "name": "Cirrhosis",
        "symptoms": "Fatigue, jaundice, abdominal swelling (ascites), easy bruising and bleeding, confusion, loss of appetite, weight loss",
        "treatments": "Treatment aims to manage symptoms, slow down disease progression, and address underlying causes. It may include: lifestyle modifications (e.g., avoiding alcohol, maintaining a healthy diet), medication (e.g., diuretics, lactulose, antiviral drugs), procedures (e.g., paracentesis, transjugular intrahepatic portosystemic shunt), liver transplantation (in severe cases)"
    },
    {
        "Code": 77,
        "name": "Thoracic Aortic Aneurysm",
        "symptoms": "Chest or back pain, shortness of breath, hoarseness, difficulty swallowing",
        "treatments": "Regular monitoring and imaging tests to assess aneurysm size and growth, lifestyle modifications (e.g., blood pressure control, avoiding smoking, managing cholesterol levels), medication (e.g., beta-blockers, ACE inhibitors) to manage blood pressure and reduce the risk of rupture, surgical intervention"
    },
    {
        "Code": 78,
        "name": "Subdural hemorrhage",
        "symptoms": "Headache, confusion, dizziness, nausea or vomiting, seizures, weakness or numbness",
        "treatments": "Immediate medical attention, close monitoring of vital signs and neurological status, diagnostic imaging (such as CT or MRI scan), potential surgical intervention (such as craniotomy or burr hole evacuation), medication to manage symptoms"
    },
    {
        "Code": 79,
        "name": "Congenital rubella",
        "symptoms": "Developmental delays, intellectual disability, hearing loss, vision problems, heart defects, liver or spleen enlargement, rash at birth",
        "treatments": "Supportive care to manage symptoms and complications, early intervention services for developmental delays, educational support, vision and hearing interventions, specialized medical care as needed"
    },
    {
        "Code": 80,
        "name": "Diabetic retinopathy",
        "symptoms": "Blurred or distorted vision, floaters, impaired color vision, dark or empty areas in the visual field, vision loss",
        "treatments": "Management of blood sugar levels, blood pressure control, cholesterol management, regular eye examinations, laser treatment , intravitreal injections of anti-VEGF medications, vitrectomy"
    },
    {
        "Code": 81,
        "name": "Fibromyalgia",
        "symptoms": "Widespread musculoskeletal pain, fatigue, sleep disturbances, cognitive difficulties (fibro fog), mood changes",
        "treatments": "Multidisciplinary approach: Medications for pain management (such as analgesics, antidepressants, and anticonvulsants), physical therapy, occupational therapy, cognitive-behavioral therapy, relaxation techniques, stress management, exercise programs"
    },
    {
        "Code": 82,
        "name": "Ischemia of the Bowel",
        "symptoms": "Severe abdominal pain, bloody stools, diarrhea, nausea, vomiting, fever, rapid heart rate, low blood pressure",
        "treatments": "diagnostic tests, intravenous fluids and medications to stabilize the patient, bowel rest, resection, bypass procedure, potential angioplasty"
    },
    {
        "Code": 83,
        "name": "Fetal Alcohol Syndrome",
        "symptoms": "Growth deficiencies, facial abnormalities, developmental delays, intellectual disability",
        "treatments": "Early intervention services for developmental delays, educational support, speech and occupational therapy, behavioral interventions, medical management of associated health issues"
    },
    {
        "Code": 84,
        "name": "Peritonitis",
        "symptoms": "Severe abdominal pain, tenderness, bloating, fever, nausea, vomiting, loss of appetite, increased heart rate",
        "treatments": "Intravenous antibiotics to treat the infection, intravenous fluids to restore hydration, drainage or removal of any underlying fluid or abscess, surgery to repair or remove the source of infection"
    },
    {
        "Code": 85,
        "name": "Abdominal Injury",
        "symptoms": "Abdominal pain, tenderness, bruising, swelling, difficulty breathing, nausea, vomiting, changes in bowel movements, blood in urine or stool",
        "treatments": "Immediate medical attention, X-ray, CT scan, ultrasound, stabilization of vital signs, pain management, observation for signs of internal bleeding, potential surgical intervention, wound care"
    },
    {
        "Code": 86,
        "name": "Acute Pancreatitis",
        "symptoms": "Severe upper abdominal pain, nausea, vomiting, fever, rapid pulse, swollen and tender abdomen, jaundice",
        "treatments": "Hospitalization, intravenous fluids to restore hydration, pain management, bowel rest, nutritional support, medications to control pain and inflammation"
    },
    {
        "Code": 87,
        "name": "Thrombophlebitis",
        "symptoms": "Redness, warmth, swelling, and tenderness along a vein, pain or discomfort, skin discoloration, visible veins, fever",
        "treatments": "Medications to manage pain and inflammation, compression stockings or bandages to promote blood flow, elevation of the affected limb, warm compresses, regular movement and exercise, treatment of underlying causes (such as infection or intravenous catheter removal), anticoagulant therapy to prevent clot formation or progression"
    },
    {
        "Code": 88,
        "name": "Asthma",
        "symptoms": "Recurrent episodes of wheezing, shortness of breath, chest tightness, coughing, especially at night or in response to triggers such as allergens or exercise",
        "treatments": "Long-term control medications (such as inhaled corticosteroids, long-acting beta-agonists), quick-relief medications (such as short-acting beta-agonists), avoidance of triggers (such as allergens, smoke), regular monitoring of symptoms and lung function, development of an asthma action plan, proper inhaler technique, regular follow-up with a healthcare provider, emergency medications (such as oral corticosteroids) as needed"
    },
    {
        "Code": 89,
        "name": "Restless Leg Syndrome",
        "symptoms": "Uncomfortable sensation in the legs, usually in the evening or at night, urge to move legs for relief",
        "treatments": "Lifestyle changes (such as regular exercise, avoiding triggers like caffeine), good sleep hygiene (maintaining a regular sleep schedule), leg massages or stretching exercises, hot or cold packs, medication therapy (such as dopamine agonists, anticonvulsants, opioids), iron supplementation (if iron deficiency is present)"
    },
    {
        "Code": 90,
        "name": "Emphysema",
        "symptoms": "Shortness of breath, wheezing, chronic cough, chest tightness, fatigue, weight loss",
        "treatments": "Smoking cessation (the most important intervention), medications to manage symptoms (such as bronchodilators, inhaled corticosteroids), pulmonary rehabilitation (exercise training, breathing techniques), supplemental oxygen therapy (in advanced cases), vaccination against respiratory infections, avoiding exposure to irritants (such as secondhand smoke or air pollutants), regular monitoring of symptoms and lung function, surgical interventions (such as lung volume reduction surgery or lung transplantation)"
    },
    {
        "Code": 91,
        "name": "Induced Abortion",
        "symptoms": "Vaginal bleeding, cramping, abdominal pain, nausea, fatigue, emotional distress",
        "treatments": "Medical Abortion: Medication (such as mifepristone and misoprostol) is used to induce abortion, which can be done in the early stages of pregnancy. Surgical Abortion: A healthcare professional performs a procedure to remove the pregnancy, which can involve suction aspiration or dilation and curettage (D&C). It's important to consult with a healthcare professional to discuss the options and determine the most suitable method."
    },
    {
        "Code": 92,
        "name": "Acute Sinusitis",
        "symptoms": "Facial pain or pressure, nasal congestion, thick nasal discharge, post-nasal drip, cough, headache, fatigue, fever (in some cases)",
        "treatments": "Home remedies (such as nasal saline irrigation, steam inhalation), over-the-counter pain relievers (such as acetaminophen or ibuprofen), nasal decongestants (for short-term use), nasal corticosteroids (to reduce inflammation), plenty of fluids and rest, warm compresses, avoidance of irritants (such as smoke or allergens), prescription antibiotics (if bacterial infection is suspected or confirmed), management of underlying causes (such as allergies or nasal polyps), symptom relief medications (such as cough suppressants or antihistamines)"
    },
    {
        "Code": 93,
        "name": "Von Hippel-Lindau Disease",
        "symptoms": "Hemangioblastomas (tumors in the brain, spinal cord, or other organs), retinal angiomas (abnormal blood vessel growth in the retina), renal cell carcinomas (kidney tumors), pheochromocytomas (adrenal gland tumors), pancreatic cysts/tumors, other tumors or cysts",
        "treatments": "Regular monitoring and surveillance to detect and manage tumor growth and associated complications, surgical removal or treatment of tumors if necessary, embolization or radiation therapy for certain tumors, medication or surgery to manage hormonal issues (such as pheochromocytomas), genetic counseling and testing, screening and management for other potential complications (such as kidney function monitoring)"
    },
    {
        "Code": 94,
        "name": "Alcohol Use Disorder",
        "symptoms": "Cravings for alcohol, inability to control or limit alcohol consumption, withdrawal symptoms (such as tremors, anxiety, sweating) when attempting to stop or reduce alcohol use, continued use despite negative consequences (such as relationship problems, health issues), neglecting responsibilities, tolerance to alcohol",
        "treatments": "Detoxification (if necessary), counseling or therapy (such as cognitive-behavioral therapy, motivational interviewing), support groups (such as Alcoholics Anonymous), medication (such as disulfiram, naltrexone, acamprosate), addressing underlying psychological or social factors, lifestyle changes, ongoing monitoring and support"
    },
    {
        "Code": 95,
        "name": "Opioid Use Disorder",
        "symptoms": "Compulsive use of opioids, strong desire or cravings for opioids, inability to control or reduce opioid use, withdrawal symptoms (such as nausea, muscle aches, anxiety) when attempting to stop or reduce use, tolerance to opioids, continued use despite negative consequences (such as legal issues, health problems)",
        "treatments": "Medication-assisted treatment (such as methadone, buprenorphine, naltrexone), counseling or therapy (such as cognitive-behavioral therapy, contingency management), support groups (such as Narcotics Anonymous), harm reduction strategies, addressing underlying psychological or social factors, lifestyle changes, ongoing monitoring and support"
    },
    {
        "Code": 96,
        "name": "Stimulant Use Disorder",
        "symptoms": "Increased energy and alertness, euphoria, decreased appetite, increased heart rate and blood pressure, insomnia, restlessness, irritability, paranoia, psychosis (in severe cases)",
        "treatments": "Counseling or therapy (such as cognitive-behavioral therapy, motivational interviewing), support groups, medication (if applicable), addressing underlying psychological or social factors, lifestyle changes, addressing co-occurring mental health conditions, harm reduction strategies, ongoing monitoring and support"
    },
    {
        "Code": 97,
        "name": "Cannabis Use Disorder",
        "symptoms": "Increased appetite, relaxation, altered perception of time, impaired memory and concentration, bloodshot eyes, anxiety or paranoia (in some individuals), withdrawal symptoms (such as irritability, insomnia) when attempting to stop or reduce cannabis use, continued use despite negative consequences (such as relationship problems, job difficulties)",
        "treatments": "Counseling or therapy (such as cognitive-behavioral therapy, motivational interviewing), support groups, addressing underlying psychological or social factors, lifestyle changes, addressing co-occurring mental health conditions, harm reduction strategies, ongoing monitoring and support"
    },
    {
        "Code": 98,
        "name": "Benzodiazepine Use Disorder",
        "symptoms": "Sedation, relaxation, reduced anxiety, drowsiness, poor coordination, memory impairment, withdrawal symptoms (such as rebound anxiety, insomnia, tremors) when attempting to stop or reduce benzodiazepine use, continued use despite negative consequences (such as relationship problems, health risks)",
        "treatments": "Gradual tapering off benzodiazepines under medical supervision, counseling or therapy (such as cognitive-behavioral therapy), support groups, addressing underlying psychological or social factors, lifestyle changes, addressing co-occurring mental health conditions, harm reduction strategies, ongoing monitoring and support"
    },
    {
        "Code": 99,
        "name": "Hallucinogen Use Disorder",
        "symptoms": "Altered perception of reality, visual or auditory hallucinations, changes in sensory experiences, introspective thoughts, feelings of connection or disconnection, anxiety or paranoia (in some individuals), flashbacks (in some individuals)",
        "treatments": "Counseling or therapy (such as cognitive-behavioral therapy, motivational interviewing), support groups, addressing underlying psychological or social factors, harm reduction strategies, ongoing monitoring and support"
    },
    {
        "Code": 100,
        "name": "Sedative, Hypnotic, or Anxiolytic Use Disorder",
        "symptoms": "Sedation, relaxation, reduced anxiety, drowsiness, poor coordination, memory impairment, withdrawal symptoms (such as rebound anxiety, insomnia, tremors) when attempting to stop or reduce use, continued use despite negative consequences (such as relationship problems, health risks)",
        "treatments": "Gradual tapering off sedatives, hypnotics, or anxiolytics under medical supervision, counseling or therapy (such as cognitive-behavioral therapy), support groups, addressing underlying psychological or social factors, lifestyle changes, addressing co-occurring mental health conditions, harm reduction strategies, ongoing monitoring and support"
    },
    {
        "Code": 101,
        "name": "Postpartum Depression",
        "symptoms": "Persistent feelings of sadness, emptiness, or hopelessness, frequent crying, irritability, loss of interest or pleasure in activities, difficulty bonding with the baby, changes in appetite or sleep patterns, overwhelming fatigue, feelings of guilt or worthlessness, trouble concentrating or making decisions, thoughts of self-harm or harming the baby",
        "treatments": "Psychotherapy (such as cognitive-behavioral therapy or interpersonal therapy), support groups or peer counseling, antidepressant medication (if recommended by a healthcare professional), hormone therapy (in some cases), lifestyle changes (such as exercise, healthy diet, sleep hygiene), involving a partner or family in the care of the baby, social support and understanding from family and friends, regular follow-up and monitoring by healthcare professionals"
    },
    {
        "Code": 102,
        "name": "Coronary Atherosclerosis",
        "symptoms": "Chest pain or discomfort (angina), shortness of breath, fatigue, irregular heartbeat, dizziness, nausea, sweating, jaw or arm pain (in some cases), heart attack (when a coronary artery becomes completely blocked)",
        "treatments": "Lifestyle changes (such as a heart-healthy diet, regular exercise, weight management, smoking cessation), medication (such as aspirin, cholesterol-lowering medications, beta-blockers, calcium channel blockers, nitroglycerin), procedures (such as angioplasty and stenting, coronary artery bypass grafting), cardiac rehabilitation, management of other risk factors (such as high blood pressure, diabetes)"
    },
    {
        "Code": 103,
        "name": "Spondylitis",
        "symptoms": "Chronic back pain and stiffness, especially in the morning or after periods of inactivity, limited range of motion in the spine, fatigue, inflammation and pain in other joints (such as hips, shoulders, knees), discomfort or pain in the neck, difficulty maintaining proper posture, tenderness or swelling in affected areas, tingling or numbness in extremities in severe cases",
        "treatments": "Medication (such as nonsteroidal anti-inflammatory drugs, corticosteroids, disease-modifying antirheumatic drugs), physical therapy (including stretching and strengthening exercises), heat or cold therapy, posture correction techniques, lifestyle modifications (such as regular exercise, weight management), assistive devices (such as braces or supports), surgical intervention (in rare cases), pain management techniques (such as acupuncture or transcutaneous electrical nerve stimulation)"
    },
    {
        "Code": 104,
        "name": "Pituitary Adenoma",
        "symptoms": "Headaches, vision problems (such as blurred vision or loss of peripheral vision), hormonal imbalances (such as excessive production or deficiency of specific hormones), fatigue, weight gain or loss, menstrual irregularities, infertility, erectile dysfunction, growth abnormalities in children, mood changes, cognitive impairments",
        "treatments": "Observation and monitoring (for small, non-secreting tumors that are not causing significant symptoms), medication (to manage hormonal imbalances or reduce tumor size), surgery (transsphenoidal surgery to remove the tumor), radiation therapy (in cases where surgery is not possible or to treat residual or recurrent tumors), targeted therapy (in cases of aggressive or resistant tumors), hormone replacement therapy (if necessary), regular follow-up and monitoring to assess tumor growth and hormone levels, management of associated complications or hormone deficiencies"
    },
    {
        "Code": 105,
        "name": "Uterine Fibroids",
        "symptoms": "Heavy or prolonged menstrual periods, pelvic pain or pressure, frequent urination, difficulty emptying the bladder, constipation, backache, leg pain, enlarged abdomen or uterus, infertility or recurrent miscarriages (in some cases)",
        "treatments": "Watchful waiting (for small or asymptomatic fibroids), medication (such as hormonal birth control, GnRH agonists, progestin-releasing intrauterine devices), minimally invasive procedures (such as uterine artery embolization, myomectomy), hysteroscopic procedures (such as hysteroscopic myomectomy or endometrial ablation), surgical removal of fibroids (such as laparoscopic or robotic-assisted myomectomy, hysterectomy), focused ultrasound ablation, hormonal therapy, alternative approaches (such as acupuncture or herbal remedies)"
    },
    {
        "Code": 106,
        "name": "Idiopathic Nonmenstrual Bleeding",
        "symptoms": "Abnormal vaginal bleeding outside of the menstrual period, unpredictable bleeding episodes, bleeding after sexual intercourse, bleeding after menopause, spotting or light bleeding between periods, prolonged or heavy bleeding",
        "treatments": "Evaluation to rule out underlying causes (such as hormonal imbalances, polyps, infections, or uterine abnormalities), hormonal therapy (such as birth control pills, hormone replacement therapy), non-hormonal medications (such as tranexamic acid), dilation and curettage (if necessary to remove excessive tissue or investigate the cause), endometrial ablation (in some cases), hysteroscopy (to examine the uterus), surgery (in rare cases), counseling or support for emotional well-being"
    },
    {
        "Code": 107,
        "name": "Chalazion",
        "symptoms": "Painful, red lump or swelling on the eyelid, usually on the upper eyelid, sensitivity to light, blurred vision (if the chalazion affects the line of sight), mild discomfort, tenderness, localized inflammation and swelling",
        "treatments": "Warm compresses (to help soften and promote drainage of the blocked oil gland), gentle massage of the affected area, eyelid hygiene (keeping the area clean), over-the-counter lubricating eye drops, topical antibiotic ointments (if there is a risk of infection), corticosteroid injections (for larger or persistent chalazia), surgical drainage or excision (in rare cases or if conservative treatments are ineffective)"
    },
    {
        "Code": 108,
        "name": "Ovarian Torsion",
        "symptoms": "Sudden and severe abdominal or pelvic pain on one side, sharp or stabbing pain, nausea, vomiting, fever, rapid heartbeat, abdominal tenderness, bloating, swelling, pain during intercourse, abnormal bleeding or spotting",
        "treatments": "Emergency medical attention (as ovarian torsion is a medical emergency), imaging tests (such as ultrasound or CT scan) to diagnose torsion, surgical intervention (laparoscopic or open surgery) to untwist the ovary and restore blood flow, removal of the ovary (if it is damaged or non-viable), pain management (medications for pain relief)"
    },
    {
        "Code": 109,
        "name": "Vaginal Yeast Infection",
        "symptoms": "Itching and irritation in the vagina and vulva, redness and swelling of the vulva, white, thick, clumpy vaginal discharge (resembling cottage cheese), burning sensation during urination, pain during sexual intercourse, rash or soreness in the affected area",
        "treatments": "Over-the-counter antifungal creams, ointments, or suppositories (such as miconazole, clotrimazole, or terconazole), prescription-strength antifungal medications (in severe or recurrent cases), oral antifungal medications (if recommended by a healthcare professional), topical corticosteroids (for relief of itching and inflammation), maintaining good hygiene practices, avoiding irritants (such as scented products), wearing breathable cotton underwear, avoiding tight-fitting clothing, probiotics (to restore healthy vaginal flora)"
    },
    {
        "Code": 110,
        "name": "Mastoiditis",
        "symptoms": "Ear pain (particularly behind the ear), swelling and redness of the ear or the area behind the ear, fever, headache, hearing loss or impaired hearing, drainage of fluid or pus from the ear, earache, irritability (in infants and young children), tenderness or pain when touching the area, mastoid bone protrusion or swelling",
        "treatments": "Antibiotics (oral or intravenous) to treat the underlying bacterial infection, pain relievers (such as acetaminophen or ibuprofen) for pain and fever, ear drops (if there is drainage from the ear), surgical intervention (in severe or chronic cases), such as mastoidectomy (removal of infected mastoid bone cells) or tympanostomy tube placement (to relieve pressure and drain fluid from the middle ear), supportive care (rest, hydration, warm compresses)"
    },
    {
        "Code": 111,
        "name": "Lung Contusion",
        "symptoms": "Chest pain (sharp or dull), difficulty breathing or shortness of breath, rapid or shallow breathing, coughing up blood or pink-tinged sputum, decreased oxygen levels, wheezing, cyanosis (bluish discoloration of the skin), chest wall bruising, rib fractures (associated injuries)",
        "treatments": "Supportive care (including supplemental oxygen, pain management, and respiratory support), monitoring in a hospital setting (to assess lung function and overall stability), treatment of associated injuries (such as rib fractures), management of complications (such as pneumonia or respiratory failure), prevention of further complications (such as deep vein thrombosis or pressure ulcers), respiratory therapy (including breathing exercises and airway clearance techniques), possible use of mechanical ventilation in severe cases"
    },
    {
        "Code": 112,
        "name": "Hypertrophic Obstructive Cardiomyopathy (HOCM)",
        "symptoms": "Shortness of breath, especially during physical activity or exertion, chest pain or discomfort, dizziness or lightheadedness, fainting or near-fainting episodes, heart palpitations (rapid or irregular heartbeat), fatigue, swelling in the ankles, feet, or legs",
        "treatments": "Medications to relieve symptoms and improve heart function (such as beta-blockers, calcium channel blockers, and disopyramide), medications to prevent abnormal heart rhythms (such as anti-arrhythmic drugs), medications to reduce blood clotting (such as aspirin or anticoagulants), implantable cardioverter-defibrillator (ICD) placement (to monitor and correct abnormal heart rhythms), septal myectomy (surgical removal of a portion of the thickened heart muscle), alcohol septal ablation (destruction of excess heart muscle with alcohol injection), lifestyle modifications (such as avoiding strenuous activities, managing stress, and maintaining a healthy weight), regular follow-up visits with a cardiologist"
    },
    {
        "Code": 113,
        "name": "Pulmonary Eosinophilia",
        "symptoms": "Cough, shortness of breath, wheezing, chest pain, fever, night sweats, fatigue, weight loss, elevated eosinophil count in the blood or sputum",
        "treatments": "Identification and treatment of underlying causes (such as parasitic infections, drug reactions, or allergic reactions), corticosteroids (such as prednisone) to reduce inflammation, bronchodilators (such as inhalers) to relieve bronchospasm and improve airflow, antiparasitic medications (if parasitic infection is identified), immunosuppressive medications (in severe cases), avoidance of triggers or allergens (if identified), symptomatic treatment for associated symptoms (such as fever or cough), regular monitoring and follow-up with a healthcare professional"
    },
    {
        "Code": 114,
        "name": "Corneal Disorder",
        "symptoms": "Blurred or hazy vision, eye pain or discomfort, redness or irritation of the eye, excessive tearing, sensitivity to light (photophobia), foreign body sensation, dryness or excessive tearing, corneal abrasions or ulcers, distorted or irregular corneal shape, vision loss",
        "treatments": "Treatment depends on the specific corneal disorder and may include: artificial tears or lubricating eye drops, antibiotic or antifungal eye drops (if infection is present), corticosteroid eye drops or ointments (to reduce inflammation), bandage contact lenses, therapeutic contact lenses, corneal transplantation (in severe cases), refractive surgeries (such as LASIK or PRK) to correct vision, protective eyewear or sunglasses, avoiding irritants or triggers, regular eye examinations and monitoring, lifestyle modifications (such as proper eye hygiene and avoiding eye strain)"
    },
    {
        "Code": 115,
        "name": "Foreign Body in the Gastrointestinal Tract",
        "symptoms": "Abdominal pain or discomfort, difficulty swallowing, choking or gagging, drooling, nausea or vomiting, loss of appetite, chest pain or pressure, respiratory distress, coughing or wheezing, gastrointestinal bleeding, bowel obstruction, perforation of the digestive tract",
        "treatments": "Observation and monitoring (for small, smooth, and non-sharp objects that are likely to pass through the digestive tract without complications), endoscopic removal (using a flexible tube with a camera to locate and remove the foreign body), surgical intervention (in cases of severe complications, large or sharp objects, or failed endoscopic removal attempts), supportive care (such as intravenous fluids, pain management, and antibiotics if infection is present), imaging studies (such as X-rays or CT scans) to evaluate the location and extent of the foreign body, consultation with a gastroenterologist or surgeon for appropriate management"
    },
    {
        "Code": 116,
        "name": "Endophthalmitis",
        "symptoms": "Eye pain, redness, swelling, blurred vision, decreased vision, floaters (dark spots or cobwebs in the vision), increased sensitivity to light (photophobia), discharge from the eye, excessive tearing, fever",
        "treatments": "Immediate medical attention is required. Treatment may include: intravenous antibiotics or antifungal medications, intravitreal injections (injections of antibiotics or antifungal agents directly into the eye), vitrectomy (surgical removal of the gel-like fluid within the eye), topical or oral medications (to manage pain, inflammation, or infection), frequent follow-up visits with an ophthalmologist, supportive care (such as warm compresses or lubricating eye drops)"
    },
    {
        "Code": 117,
        "name": "Achalasia",
        "symptoms": "Difficulty swallowing",
        "treatments": "Balloon dilation, surgery, medication"
    },
    {
        "Code": 118,
        "name": "Conductive Hearing Loss",
        "symptoms": "Reduced hearing sensitivity, muffled or blocked sound",
        "treatments": "Medications, surgical intervention, hearing aids"
    },
    {
        "Code": 119,
        "name": "Abdominal Hernia",
        "symptoms": "Visible bulge or swelling, discomfort or pain",
        "treatments": "Watchful waiting, hernia truss, surgical repair, lifestyle changes"
    },
    {
        "Code": 120,
        "name": "Marijuana Abuse",
        "symptoms": "Impaired memory and cognition, altered judgment, anxiety",
        "treatments": "Behavioral therapy, counseling, support groups, medication, detoxification"
    },
    {
        "Code": 121,
        "name": "Cryptococcosis",
        "symptoms": "Headache, fever, fatigue, cough, meningitis, pneumonia",
        "treatments": "Antifungal medication (e.g., Amphotericin B, Fluconazole), supportive care"
    },
    {
        "Code": 122,
        "name": "Obesity",
        "symptoms": "Excessive body weight, increased risk of chronic conditions",
        "treatments": "Antifungal medication eg  Amphotericin B, Fluconazole, supportive care"
    },
    {
        "Code": 123,
        "name": "Indigestion",
        "symptoms": "Abdominal pain, bloating, heartburn, nausea, acidic taste",
        "treatments": "Lifestyle changes (e.g., dietary modifications, stress reduction), over-the-counter antacids, medication, therapy"
    },
    {
        "Code": 124,
        "name": "Bursitis",
        "symptoms": "Joint pain, swelling, tenderness, limited range of motion",
        "treatments": "Rest, ice, compression, elevation (RICE therapy), pain relievers, physical therapy, steroid injections"
    },
    {
        "Code": 125,
        "name": "Esophageal Cancer",
        "symptoms": "Difficulty swallowing, unintentional weight loss, chest pain, hoarseness",
        "treatments": "Surgery, chemotherapy, radiation therapy, targeted therapy, immunotherapy, palliative care, clinical trials"
    },
    {
        "Code": 126,
        "name": "Pulmonary Congestion",
        "symptoms": "Shortness of breath, cough, wheezing, fatigue, chest discomfort or tightness",
        "treatments": "Diuretics, medications to manage underlying conditions (e.g., heart failure), oxygen therapy, lifestyle changes"
    },
    {
        "Code": 127,
        "name": "Juvenile Rheumatoid Arthritis",
        "symptoms": "Joint pain, swelling, stiffness, limited range of motion, fever, rash",
        "treatments": "Medications (NSAIDs, DMARDs), physical therapy, occupational therapy, exercise, assistive devices"
    },
    {
        "Code": 128,
        "name": "Actinic Keratosis",
        "symptoms": "Rough, scaly patches on the skin, usually in sun-exposed areas",
        "treatments": "Topical medications (e.g., fluorouracil, imiquimod, diclofenac), cryotherapy, curettag"
    },
    {
        "Code": 129,
        "name": "Acute Otitis Media",
        "symptoms": "Ear pain, fever, fluid drainage from the ear, hearing loss or muffled hearing in the affected ear",
        "treatments": "Antibiotics, pain relievers (e.g., acetaminophen, ibuprofen), warm compresses, ear drops, tympanostomy tubes (in some cases)"
    },
    {
        "Code": 130,
        "name": "Astigmatism",
        "symptoms": "Blurred or distorted vision, eye strain, headaches,uneven curvature of cornea",
        "treatments": "Eyeglasses, contact lenses, refractive surgery (LASIK, PRK), orthokeratology, toric intraocular lenses"
    },
    {
        "Code": 131,
        "name": "Tuberous Sclerosis",
        "symptoms": "Benign tumors in various organs, seizures, developmental delays, skin abnormalities",
        "treatments": "Medications (anti-seizure, behavioral, etc.), surgery (for tumor removal), therapy (physical, occupational, speech), educational interventions, support services, genetic counseling, monitoring of organ involvement"
    },
    {
        "Code": 132,
        "name": "Empyema",
        "symptoms": "Fever, chest pain, productive cough with foul-smelling or bloody sputum",
        "treatments": "Antibiotics, drainage (chest tube insertion, thoracentesis), surgical intervention (decortication), supportive care, treatment of underlying cause"
    },
    {
        "Code": 133,
        "name": "Presbycusis",
        "symptoms": "Gradual hearing loss, difficulty hearing high-pitched sounds, speech sounds muffled or unclear",
        "treatments": "Hearing aids, assistive listening devices, cochlear implants (in severe cases), communication strategies, counseling, regular hearing evaluations"
    },
    {
        "Code": 134,
        "name": "Neonatal Jaundice",
        "symptoms": "Yellowing of the skin and eyes, pale stools, dark urine",
        "treatments": "Phototherapy, exchange transfusion (in severe cases), monitoring of bilirubin levels, addressing underlying causes (e.g., breastfeeding)"
    },
    {
        "Code": 135,
        "name": "Dislocation of the Elbow",
        "symptoms": "Severe pain, visible deformity, swelling, inability to move the elbow, numbness or tingling in the hand/arm",
        "treatments": "Closed reduction (realigning the bones without surgery), immobilization (splint or cast), physical therapy, pain management, surgical intervention (in complex or recurrent cases)"
    },
    {
        "Code": 136,
        "name": "Spondylosis",
        "symptoms": "Neck or back pain, stiffness, limited range of motion, numbness or weakness in the extremities",
        "treatments": "Medications (pain relievers, muscle relaxants), physical therapy, exercise, posture improvement, heat or cold therapy, spinal injections, surgery (in severe cases or if conservative treatments fail)"
    },
    {
        "Code": 137,
        "name": "Herpangina",
        "symptoms": "Sore throat, fever, painful sores or blisters in the mouth and throat, difficulty swallowing, loss of appetite",
        "treatments": "Symptomatic relief (pain relievers, throat lozenges, mouth rinses), rest, fluids, maintaining good oral hygiene, avoiding spicy or acidic foods"
    },
    {
        "Code": 138,
        "name": "Poisoning due to Antidepressants",
        "symptoms": "Nausea, vomiting, drowsiness, dizziness, confusion, seizures, changes in heart rate, low blood pressure, respiratory distress",
        "treatments": "Seek immediate medical assistance or contact a poison control center, activated charcoal (if indicated), supportive care (maintaining vital signs, airway management), gastric lavage (in certain cases), administration of antidotes (if available and appropriate), monitoring and management of complications"
    },
    {
        "Code": 139,
        "name": "Infection of Open Wound",
        "symptoms": "Redness, swelling, warmth, pain or tenderness at the wound site, pus or drainage from the wound, fever, malaise",
        "treatments": "Cleaning and irrigation of the wound, antibiotic therapy (oral or intravenous), wound dressings, wound debridement (if necessary), tetanus prophylaxis"
    },
    {
        "Code": 140,
        "name": "Protein Deficiency",
        "symptoms": "Muscle wasting, fatigue, weakness, delayed wound healing, swelling of the limbs, hair loss, impaired immunity",
        "treatments": "Increasing protein intake through diet (lean meats, fish, dairy, legumes, nuts), protein supplements, nutritional counseling, addressing underlying causes (e.g., malabsorption)"
    },
    {
        "Code": 141,
        "name": "Myoclonus",
        "symptoms": "Sudden, brief muscle contractions or jerks, often affecting the arms, legs, or face",
        "treatments": "Identifying and treating underlying causes (e.g., medication adjustments, metabolic imbalances), medications (anti-seizure drugs, tranquilizers), physical therapy, supportive care"
    },
    {
        "Code": 142,
        "name": "Bone Spur of the Calcaneus",
        "symptoms": "Heel pain, especially when walking or standing, tenderness, swelling, inflammation of the surrounding tissue",
        "treatments": "Nonsteroidal anti-inflammatory drugs (NSAIDs), orthotic devices, physical therapy, stretching exercises, shoe modifications, corticosteroid injections, surgical removal (in severe cases)"
    },
    {
        "Code": 143,
        "name": "Von Willebrand Disease",
        "symptoms": "Easy or excessive bruising, prolonged or excessive bleeding from cuts or injuries, frequent nosebleeds, heavy or prolonged menstrual periods, bleeding gums, blood in urine or stool",
        "treatments": "Desmopressin (DDAVP) medication, replacement therapy with von Willebrand factor (VWF) concentrate or cryoprecipitate, oral contraceptives (for women with heavy menstrual bleeding), avoiding certain medications, dental care precautions, regular medical follow-up"
    },
    {
        "Code": 144,
        "name": "Heart Block",
        "symptoms": "Fatigue, dizziness, fainting, chest pain or discomfort, shortness of breath, irregular heart rhythms",
        "treatments": "Medications (such as beta-blockers, calcium channel blockers), pacemaker implantation (in severe cases or symptomatic heart block), underlying condition management"
    },
    {
        "Code": 145,
        "name": "Colonic Polyp",
        "symptoms": "Most colonic polyps do not cause symptoms. Some larger polyps or certain types may cause rectal bleeding or changes in bowel habits, such as diarrhea or constipation.",
        "treatments": "Polypectomy (removal of polyp during colonoscopy), surveillance colonoscopy (regular monitoring for recurrence or new polyps), lifestyle modifications (healthy diet, regular exercise, smoking cessation), follow-up based on pathology findings"
    },
    {
        "Code": 146,
        "name": "Hypospadias",
        "symptoms": "Abnormal positioning of the urethral opening on the underside of the penis, penile curvature, spraying of urine, difficulty in urination",
        "treatments": "Surgical repair (hypospadias repair surgery), hormone therapy (in some cases), counseling and support for the child and family"
    },
    {
        "Code": 147,
        "name": "Magnesium Deficiency",
        "symptoms": "Muscle twitches or cramps, fatigue, weakness, loss of appetite, nausea, vomiting, irritability, mental confusion, irregular heartbeat, tingling or numbness, personality changes, seizures",
        "treatments": "Dietary changes (consuming magnesium-rich foods), oral magnesium supplements, intravenous magnesium therapy (in severe cases), addressing underlying causes (e.g., malabsorption), medical supervision and monitoring"
    },
    {
        "Code": 148,
        "name": "Female Infertility of Unknown Cause",
        "symptoms": "Inability to conceive after one year of unprotected intercourse, irregular or absent menstrual cycles, hormonal imbalances, age-related factors, other",
        "treatments": "Fertility testing and evaluation (hormone tests, imaging, genetic screening), lifestyle modifications (healthy diet, regular exercise, stress reduction), fertility treatments (assisted reproductive technologies, fertility medications)"
    },
    {
        "Code": 149,
        "name": "Pericarditis",
        "symptoms": "Chest pain (sharp and stabbing), worsens with deep breaths or lying down, fever",
        "treatments": "Nonsteroidal anti-inflammatory drugs (NSAIDs) to reduce inflammation and pain, colchicine (for recurrent or persistent pericarditis), corticosteroids (in severe cases or when NSAIDs are ineffective), antibiotics (if bacterial infection is present), lifestyle modifications (rest, avoiding strenuous activity), treating underlying causes (if identified), potential pericardiocentesis (fluid drainage)"
    },
    {
        "Code": 150,
        "name": "Attention Deficit Hyperactivity Disorder (ADHD)",
        "symptoms": "Inattention, hyperactivity, impulsivity",
        "treatments": "Behavioral therapy, parent training programs, medication (such as stimulants or non-stimulants), individualized education plans (IEPs) for academic support, accommodations and modifications in school, psychoeducation, counseling"
    },
    {
        "Code": 151,
        "name": "Neuromyelitis Optica",
        "symptoms": "Optic neuritis (vision loss, pain with eye movement), transverse myelitis (weakness, numbness, or paralysis of the limbs, loss of bladder or bowel control)",
        "treatments": "High-dose corticosteroids, plasma exchange (to remove antibodies from the blood), immunosuppressive therapy (such as azathioprine or rituximab), supportive care to manage symptoms, physical therapy or rehabilitation for functional recovery"
    },
    {
        "Code": 152,
        "name": "Pulmonic Valve Disease",
        "symptoms": "Fatigue, shortness of breath, chest pain or discomfort, heart palpitations, fainting or lightheadedness, swollen legs or ankles",
        "treatments": "Medications (such as diuretics, beta-blockers, or calcium channel blockers), surgical interventions (such as balloon valvuloplasty or valve replacement), lifestyle modifications (such as regular exercise, heart-healthy diet, smoking cessation), regular follow-up with a cardiologist"
    },
    {
        "Code": 153,
        "name": "Tietze Syndrome",
        "symptoms": "Chest pain, swelling and tenderness of the cartilage connecting the ribs to the breastbone",
        "treatments": "Nonsteroidal anti-inflammatory drugs (NSAIDs), pain relievers, local heat or ice application, avoiding activities that worsen symptoms, supportive measures (such as wearing loose clothing or using supportive pillows), physical therapy (to improve posture and strengthen muscles), corticosteroid injections (in some cases), stress reduction techniques"
    },
    {
        "Code": 154,
        "name": "Cranial Nerve Palsy",
        "symptoms": "Depends on the specific cranial nerve involved; symptoms can include vision changes, eye movement abnormalities, facial weakness or paralysis, difficulty swallowing or speaking, loss of sensation in the face or other areas",
        "treatments": "Treatment depends on the underlying cause and specific cranial nerve affected. It may include medications (such as corticosteroids or antiviral drugs), physical therapy, speech therapy, occupational therapy, eye exercises, surgery (in some cases), and management of any underlying conditions."
    },
    {
        "Code": 155,
        "name": "Conversion Disorder",
        "symptoms": "Neurological symptoms that cannot be explained by a medical condition or injury, such as paralysis, blindness, seizures, or difficulty speaking",
        "treatments": "Psychotherapy (such as cognitive-behavioral therapy or psychodynamic therapy), physical therapy or rehabilitation (to improve physical function and reduce disability), addressing underlying stressors or psychological factors, supportive care and reassurance, potentially medications (such as antidepressants or anti-anxiety medications)"
    },
    {
        "Code": 156,
        "name": "Complex Regional Pain Syndrome",
        "symptoms": "Severe and chronic pain, often in the limbs, with associated swelling, changes in skin color or temperature, abnormal sweating, limited range of motion",
        "treatments": "Physical therapy (including exercises, stretching, and mirror therapy), pain management techniques (such as medications, nerve blocks, or spinal cord stimulation), sympathetic nerve blocks, psychological support (such as cognitive-behavioral therapy or counseling), occupational therapy, graded motor imagery, transcutaneous electrical nerve stimulation (TENS), patient education and self-management techniques"
    },
    {
        "Code": 157,
        "name": "Otosclerosis",
        "symptoms": "Hearing loss (gradual and progressive), tinnitus (ringing in the ears), dizziness or balance problems",
        "treatments": "Hearing aids, surgical interventions (such as stapedectomy or stapedotomy to replace the affected bone in the middle ear), sodium fluoride therapy (to slow down the progression of the condition), communication strategies and support (such as lip-reading or sign language), regular hearing assessments"
    },
    {
        "Code": 158,
        "name": "Hypothyroidism",
        "symptoms": "Fatigue, weight gain, sensitivity to cold, dry skin, constipation, depression, muscle weakness, elevated cholesterol levels",
        "treatments": "Hormone replacement therapy with synthetic thyroid hormone (levothyroxine), regular monitoring of thyroid hormone levels and adjustment of medication dosage, lifestyle modifications (such as healthy diet and regular exercise), management of associated symptoms (such as cholesterol-lowering medications or antidepressants), education and support for long-term management"
    },
    {
        "Code": 159,
        "name": "Primary Insomnia",
        "symptoms": "Difficulty falling asleep or staying asleep, daytime sleepiness, irritability, difficulty concentrating",
        "treatments": "Cognitive-behavioral therapy for insomnia (CBT-I), sleep hygiene practices (such as maintaining a regular sleep schedule, creating a comfortable sleep environment), relaxation techniques, stimulus control techniques (such as limiting bed activities to sleep only), sleep restriction therapy, medications for insomnia (such as sedative-hypnotics, melatonin agonists)"
    },
    {
        "Code": 160,
        "name": "Lice",
        "symptoms": "Itching and visible presence of lice or nits (eggs) in the hair",
        "treatments": "Over-the-counter or prescription medications specifically designed to kill lice (such as pediculicides), manual removal of lice and nits using a fine-toothed comb, washing and drying of infested clothing and bedding at high temperatures, vacuuming of upholstery and household surfaces, disinfection of personal items that cannot be washed or dried, avoiding direct head-to-head contact with infested individuals, education and prevention strategies"
    },
    {
        "Code": 161,
        "name": "Vitamin B12 Deficiency",
        "symptoms": "Fatigue, weakness, pale skin, shortness of breath, tingling or numbness in the hands and feet, balance problems, sore tongue",
        "treatments": "Vitamin B12 supplementation (such as oral supplements or injections), dietary changes to include B12-rich foods (such as meat, fish, eggs, and dairy products), identification and management of underlying causes (such as pernicious anemia or malabsorption disorders), management of associated symptoms or complications (such as nerve pain or balance problems), regular monitoring of B12 levels and treatment adjustment"
    },
    {
        "Code": 162,
        "name": "Vulvodynia",
        "symptoms": "Persistent pain or discomfort in the vulva, burning, stinging, rawness, itching",
        "treatments": "Topical medications (such as lidocaine or estrogen creams), nerve blocks, physical therapy (including pelvic floor muscle relaxation exercises), cognitive-behavioral therapy (CBT), biofeedback, medications (such as tricyclic antidepressants or anticonvulsants), vulvar care and hygiene practices, stress management techniques, alternative therapies (such as acupuncture or herbal remedies)"
    },
    {
        "Code": 163,
        "name": "Endometriosis",
        "symptoms": "Pelvic pain (during menstruation, intercourse, or bowel movements), heavy menstrual bleeding, infertility",
        "treatments": "Pain management (such as nonsteroidal anti-inflammatory drugs [NSAIDs], hormonal contraceptives, or progestins), hormone therapy (such as gonadotropin-releasing hormone [GnRH] agonists or oral contraceptives), surgical interventions (such as laparoscopic excision or hysterectomy), fertility treatments (if pregnancy is desired), lifestyle modifications (such as regular exercise, stress management), complementary therapies (such as acupuncture or dietary changes)"
    },
    {
        "Code": 164,
        "name": "Vasculitis",
        "symptoms": "Inflammation of blood vessels leading to various symptoms depending on the affected organs, including rash, fever, fatigue, muscle and joint pain, shortness of breath, weight loss",
        "treatments": "Treatment depends on the type and severity of vasculitis. It may include corticosteroids, immunosuppressive medications (such as cyclophosphamide or azathioprine), biologic therapies (such as rituximab), disease-specific treatments (such as plasmapheresis for certain types), supportive care to manage symptoms (such as pain relievers or blood pressure medications), monitoring and management of associated complications (such as organ damage or infections)"
    },
    {
        "Code": 165,
        "name": "Concussion",
        "symptoms": "Headache, dizziness, nausea or vomiting, confusion, memory problems, sensitivity to light or noise, mood changes",
        "treatments": "Physical and cognitive rest, gradual return to normal activities, symptom management (such as pain relievers or anti-nausea medication), monitoring for complications (such as changes in neurological function), cognitive rehabilitation (if persistent cognitive problems), management of associated symptoms (such as sleep disturbances or mood changes), education and support for recovery, avoiding further head injuries"
    },
    {
        "Code": 166,
        "name": "Oral Leukoplakia",
        "symptoms": "White patches or plaques in the mouth, often on the tongue or inside of the cheeks, that cannot be scraped off",
        "treatments": "Regular monitoring and follow-up, identification and elimination of potential irritants (such as tobacco or alcohol), improving oral hygiene practices, medication (such as topical retinoids or antifungal agents), surgical removal (in some cases), cryotherapy (freezing the patches), laser therapy, lifestyle modifications (such as healthy diet), regular dental check-ups, education and support"
    },
    {
        "Code": 167,
        "name": "Chronic Kidney Disease",
        "symptoms": "Fatigue, swelling of the legs or ankles, decreased appetite, difficulty concentrating, increased urination or urine changes, blood in urine, high blood pressure",
        "treatments": "Management of underlying conditions (such as diabetes or high blood pressure), lifestyle modifications (such as healthy diet, regular exercise, smoking cessation), medications (such as ACE inhibitors or diuretics), dialysis (in advanced stages), kidney transplant (in end-stage kidney disease), management of associated complications (such as anemia or bone disease), regular monitoring and follow-up with a nephrologist, education and support for self-care"
    },
    {
        "Code": 168,
        "name": "Bladder Disorder",
        "symptoms": "Frequent urination, urgency, pelvic pain",
        "treatments": "Medications, bladder training, lifestyle changes"
    },
    {
        "Code": 169,
        "name": "Chorioretinitis",
        "symptoms": "Eye pain, blurred vision, sensitivity to light",
        "treatments": "Antiviral medications, corticosteroids, eye drops"
    },
    {
        "Code": 170,
        "name": "Priapism",
        "symptoms": "Persistent, painful erection",
        "treatments": "Medical intervention (aspiration, medication, surgery)"
    },
    {
        "Code": 171,
        "name": "Myositis",
        "symptoms": "Muscle weakness, pain, inflammation",
        "treatments": "Medications (corticosteroids, immunosuppressants), physical therapy"
    },
    {
        "Code": 172,
        "name": "Mononucleosis",
        "symptoms": "Fatigue, sore throat, swollen lymph nodes",
        "treatments": "Rest, pain relievers, fluids, symptom management"
    },
    {
        "Code": 173,
        "name": "Neuralgia",
        "symptoms": "Sharp, shooting pain along the affected nerve",
        "treatments": "Medications (pain relievers, anticonvulsants), nerve blocks"
    },
    {
        "Code": 174,
        "name": "Polycystic Kidney Disease",
        "symptoms": "Abdominal pain, high blood pressure, kidney cysts",
        "treatments": "Symptom management, blood pressure control, dialysis"
    },
    {
        "Code": 175,
        "name": "Bipolar Disorder",
        "symptoms": "Mood swings, manic episodes, depressive episodes",
        "treatments": "Medications (mood stabilizers, antipsychotics), therapy"
    },
    {
        "Code": 176,
        "name": "Amyloidosis",
        "symptoms": "Fatigue, weight loss, organ dysfunction",
        "treatments": "Treatment depends on the type and extent of organ damage"
    },
    {
        "Code": 177,
        "name": "Chronic Inflammatory Demyelinating Polyneuropathy (CIDP)",
        "symptoms": "Weakness, numbness, tingling in limbs",
        "treatments": "Immunoglobulin therapy, corticosteroids, physical therapy"
    },
    {
        "Code": 178,
        "name": "Gastroesophageal Reflux Disease (GERD)",
        "symptoms": "Heartburn, acid reflux, chest pain",
        "treatments": "Lifestyle changes, medications (antacids, proton pump inhibitors)"
    },
    {
        "Code": 179,
        "name": "Vitreous Hemorrhage",
        "symptoms": "Floaters in vision, blurry vision, eye pain",
        "treatments": "Observation, laser treatment, vitrectomy (in severe cases)"
    },
    {
        "Code": 180,
        "name": "Antimicrobial Drugs Poisoning",
        "symptoms": "Nausea, vomiting, diarrhea, neurological symptoms",
        "treatments": "Immediate medical attention, supportive care, antidote administration"
    },
    {
        "Code": 181,
        "name": "Scleroderma",
        "symptoms": "Thickening of the skin, Raynaud's phenomenon",
        "treatments": "Medications (immunosuppressants), therapy, symptom management"
    },
    {
        "Code": 182,
        "name": "Myasthenia Gravis",
        "symptoms": "Muscle weakness, fatigue, difficulty speaking",
        "treatments": "Medications (acetylcholinesterase inhibitors, immunosuppressants), thymectomy (in some cases)"
    },
    {
        "Code": 183,
        "name": "Hypoglycemia",
        "symptoms": "Shaking, dizziness, confusion, sweating",
        "treatments": "Consuming glucose or sugar-containing foods, adjusting medication or insulin dosage"
    },
    {
        "Code": 184,
        "name": "Idiopathic Absence of Menstruation",
        "symptoms": "Lack of menstrual periods",
        "treatments": "Evaluation to determine underlying cause, hormone therapy"
    },
    {
        "Code": 185,
        "name": "Dislocation of the Ankle",
        "symptoms": "Swelling, severe pain, inability to bear weight",
        "treatments": "Reduction (realigning the bones), immobilization, rehab"
    },
    {
        "Code": 186,
        "name": "Carbon Monoxide Poisoning",
        "symptoms": "Headache, dizziness, nausea, confusion",
        "treatments": "Fresh air, oxygen therapy, immediate medical attention"
    },
    {
        "Code": 187,
        "name": "Panic Attack",
        "symptoms": "Chest pain, shortness of breath, palpitations",
        "treatments": "Breathing exercises, relaxation techniques, therapy"
    },
    {
        "Code": 188,
        "name": "Plantar Fasciitis",
        "symptoms": "Heel pain, tenderness, difficulty walking",
        "treatments": "Rest, stretching exercises, orthotic devices, physiotherapy"
    },
    {
        "Code": 189,
        "name": "Hyperopia",
        "symptoms": "Difficulty seeing objects up close, blurred vision when focusing on near objects",
        "treatments": "Eyeglasses, contact lenses, refractive surgery"
    },
    {
        "Code": 190,
        "name": "Sedatives Poisoning",
        "symptoms": "Drowsiness, confusion, slowed breathing",
        "treatments": "Immediate medical attention, supportive care, antidote administration"
    },
    {
        "Code": 191,
        "name": "Pemphigus",
        "symptoms": "Painful blisters on the skin and mucous membranes",
        "treatments": "Corticosteroids, immunosuppressants, wound care"
    },
    {
        "Code": 192,
        "name": "Peyronie Disease",
        "symptoms": "Curvature of the penis, pain during erections",
        "treatments": "Medications, traction therapy, surgery"
    },
    {
        "Code": 193,
        "name": "Hiatal Hernia",
        "symptoms": "Heartburn, chest pain, difficulty swallowing",
        "treatments": "Lifestyle changes, medications (antacids, proton pump inhibitors)"
    },
    {
        "Code": 194,
        "name": "Extrapyramidal Effect of Drugs",
        "symptoms": "Muscle stiffness, tremors, involuntary movements",
        "treatments": "Adjusting medication dosage, switching to alternative medications"
    },
    {
        "Code": 195,
        "name": "Meniere Disease",
        "symptoms": "Vertigo, hearing loss, tinnitus, ear fullness",
        "treatments": "Medications (diuretics, anti-vertigo drugs), lifestyle changes"
    },
    {
        "Code": 196,
        "name": "Anal Fissure",
        "symptoms": "Pain during bowel movements, rectal bleeding",
        "treatments": "Stool softeners, fiber supplements, topical ointments, surgical procedures (in severe cases)"
    },
    {
        "Code": 197,
        "name": "Chronic Otitis Media",
        "symptoms": "Ear pain, hearing loss, recurrent ear infections",
        "treatments": "Antibiotics, ear drops, surgical intervention (in some cases)"
    },
    {
        "Code": 198,
        "name": "Hirschsprung Disease",
        "symptoms": "Chronic constipation, abdominal distension, failure to pass meconium (in newborns)",
        "treatments": "Surgery to remove the affected part of the colon (pull-through procedure)"
    },
    {
        "Code": 199,
        "name": "Polymyalgia Rheumatica",
        "symptoms": "Muscle pain and stiffness, joint pain, fatigue",
        "treatments": "Low-dose corticosteroids, nonsteroidal anti-inflammatory drugs (NSAIDs)"
    },
    {
        "Code": 200,
        "name": "Lymphedema",
        "symptoms": "Swelling in arms or legs, feeling of heaviness or tightness",
        "treatments": "Compression therapy, exercise, lymphatic drainage techniques, surgery (in severe cases)"
    },
    {
        "Code": 201,
        "name": "Bladder Cancer",
        "symptoms": "Blood in urine, frequent urination, pelvic pain",
        "treatments": "Surgery, chemotherapy, radiation therapy"
    },
    {
        "Code": 202,
        "name": "Acute Bronchospasm",
        "symptoms": "Wheezing, shortness of breath, chest tightness",
        "treatments": "Bronchodilators (inhaled medications), corticosteroids, supplemental oxygen (if needed)"
    },
    {
        "Code": 203,
        "name": "Acute Glaucoma",
        "symptoms": "Severe eye pain, blurred vision, halos around lights",
        "treatments": "Medications (eye drops), laser therapy, surgery (in some cases)"
    },
    {
        "Code": 204,
        "name": "Dislocation of the Patella",
        "symptoms": "Knee pain, swelling, inability to straighten the leg",
        "treatments": "Manual reduction, immobilization, physical therapy"
    },
    {
        "Code": 205,
        "name": "Sciatica",
        "symptoms": "Pain radiating from the lower back to the leg",
        "treatments": "Pain medications, physical therapy, stretching exercises"
    },
    {
        "Code": 206,
        "name": "Hypercalcemia",
        "symptoms": "Fatigue, nausea, excessive thirst, kidney stones",
        "treatments": "Treating underlying cause, hydration, medications"
    },
    {
        "Code": 207,
        "name": "Stress Incontinence",
        "symptoms": "Unintentional urine leakage during physical activity",
        "treatments": "Pelvic floor exercises, behavioral techniques, surgery (in severe cases)"
    },
    {
        "Code": 208,
        "name": "Benign Kidney Cyst",
        "symptoms": "Abdominal or flank pain, blood in urine, frequent urination",
        "treatments": "Observation, medication (if needed), surgery (in rare cases)"
    },
    {
        "Code": 209,
        "name": "Hydrocele of the Testicle",
        "symptoms": "Swelling of the scrotum",
        "treatments": "Observation, surgical drainage (in some cases)"
    },
    {
        "Code": 210,
        "name": "Hirsutism",
        "symptoms": "Excessive hair growth in women",
        "treatments": "Medications (anti-androgens, oral contraceptives), hair removal methods, lifestyle changes"
    },
    {
        "Code": 211,
        "name": "Hydronephrosis",
        "symptoms": "Flank pain, urinary frequency, swelling in the abdomen",
        "treatments": "Treating underlying cause, medications, ureteral stent, surgery"
    },
    {
        "Code": 212,
        "name": "Diverticulosis",
        "symptoms": "Abdominal pain, bloating, changes in bowel movements",
        "treatments": "High-fiber diet, medications (pain relievers, antibiotics)"
    },
    {
        "Code": 213,
        "name": "Pain after an Operation",
        "symptoms": "Surgical site pain, discomfort, swelling",
        "treatments": "Pain medications, ice packs, rest, wound care"
    },
    {
        "Code": 214,
        "name": "Huntington Disease",
        "symptoms": "Motor, cognitive, and psychiatric symptoms",
        "treatments": "Supportive care, medications (to manage symptoms), therapy"
    },
    {
        "Code": 215,
        "name": "West Nile Virus",
        "symptoms": "Fever, headache, body aches, rash",
        "treatments": "Supportive care, symptom management, prevention of mosquito bites"
    },
    {
        "Code": 216,
        "name": "Lymphoma",
        "symptoms": "Swollen lymph nodes, unexplained weight loss, fatigue",
        "treatments": "Chemotherapy, radiation therapy, immunotherapy, targeted therapy"
    },
    {
        "Code": 217,
        "name": "Dermatitis due to Sun Exposure",
        "symptoms": "Redness, itching, rash, blistering",
        "treatments": "Topical corticosteroids, moisturizers, avoiding sun exposure"
    },
    {
        "Code": 218,
        "name": "Anemia due to Chronic Kidney Disease",
        "symptoms": "Fatigue, weakness, pale skin",
        "treatments": "Erythropoiesis-stimulating agents (ESA), iron supplementation, blood transfusions (in severe cases)"
    },
    {
        "Code": 219,
        "name": "Injury to Internal Organ",
        "symptoms": "Abdominal pain, bleeding, organ dysfunction",
        "treatments": "Immediate medical attention, diagnostic tests, surgery (in some cases)"
    },
    {
        "Code": 220,
        "name": "Scleritis",
        "symptoms": "Eye redness, severe eye pain, blurred vision",
        "treatments": "Steroid eye drops, nonsteroidal anti-inflammatory drugs (NSAIDs), immunosuppressants"
    },
    {
        "Code": 221,
        "name": "Pterygium",
        "symptoms": "Growth on the conjunctiva (white part of the eye)",
        "treatments": "Artificial tears, eye lubricants, surgical removal (in severe cases)"
    },
    {
        "Code": 222,
        "name": "Fungal Infection of the Skin",
        "symptoms": "Rash, itching, redness, peeling skin",
        "treatments": "Antifungal creams, powders, or oral medications, proper hygiene and skin care"
    },
    {
        "Code": 223,
        "name": "Insulin Overdose",
        "symptoms": "Low blood sugar (hypoglycemia) symptoms (e.g., confusion, sweating)",
        "treatments": "Immediate treatment of hypoglycemia, medical assistance, adjusting insulin dosage and regimen"
    },
    {
        "Code": 224,
        "name": "Syndrome of Inappropriate Secretion of ADH (SIADH)",
        "symptoms": "Excessively concentrated urine, low blood sodium levels",
        "treatments": "Treating underlying cause, fluid restriction, medications to suppress ADH (vasopressin) secretion, addressing electrolyte imbalance"
    },
    {
        "Code": 225,
        "name": "Premenstrual Tension Syndrome",
        "symptoms": "Mood swings, bloating, breast tenderness, irritability",
        "treatments": "Lifestyle changes, medications (pain relievers, hormonal contraceptives), therapy"
    },
    {
        "Code": 226,
        "name": "Orbital Cellulitis",
        "symptoms": "Eye pain, swelling, redness, vision changes",
        "treatments": "Antibiotics, hospitalization (in severe cases), surgical drainage (in some cases)"
    },
    {
        "Code": 227,
        "name": "Injury to the Leg",
        "symptoms": "Pain, swelling, bruising, difficulty walking",
        "treatments": "R.I.C.E. (Rest, Ice, Compression, Elevation), pain medications, physical therapy"
    },
    {
        "Code": 228,
        "name": "Hepatic Encephalopathy",
        "symptoms": "Confusion, forgetfulness, personality changes, tremors",
        "treatments": "Treating underlying liver disease, medications to manage symptoms, dietary modifications"
    },
    {
        "Code": 229,
        "name": "Bone Cancer",
        "symptoms": "Bone pain, fractures, fatigue, unexplained weight loss",
        "treatments": "Surgery, chemotherapy, radiation therapy, targeted therapy"
    },
    {
        "Code": 230,
        "name": "Leishmaniasis",
        "symptoms": "Skin sores, fever, weight loss, enlarged spleen or liver",
        "treatments": "Antiparasitic medications, treatment of complications, vector control measures (in endemic areas)"
    },
    {
        "Code": 231,
        "name": "Chagas Disease",
        "symptoms": "Fever, fatigue, body aches, heart and digestive problems",
        "treatments": "Antiparasitic medications, medications to manage symptoms, supportive care"
    },
    {
        "Code": 232,
        "name": "Syringomyelia",
        "symptoms": "Muscle weakness, loss of sensation, chronic pain",
        "treatments": "Surgical decompression, draining of syrinx (cyst), physical therapy, pain management techniques"
    },
    {
        "Code": 233,
        "name": "Pulmonary Fibrosis",
        "symptoms": "Shortness of breath, dry cough, fatigue",
        "treatments": "Medications (immunosuppressants, antifibrotic drugs), oxygen therapy, lung transplantation"
    },
    {
        "Code": 234,
        "name": "Mitral Valve Disease",
        "symptoms": "Fatigue, shortness of breath, heart palpitations",
        "treatments": "Medications, lifestyle changes, surgical repair or replacement of the valve (in severe cases)"
    },
    {
        "Code": 235,
        "name": "Parkinson Disease",
        "symptoms": "Tremors, stiffness, slowness of movement",
        "treatments": "Medications (levodopa, dopamine agonists), physical therapy, deep brain stimulation"
    },
    {
        "Code": 236,
        "name": "Gout",
        "symptoms": "Intense joint pain, swelling, redness",
        "treatments": "Medications (nonsteroidal anti-inflammatory drugs, colchicine), lifestyle changes"
    },
    {
        "Code": 237,
        "name": "Otitis Media",
        "symptoms": "Ear pain, fever, fluid drainage from the ear",
        "treatments": "Antibiotics (if bacterial infection), pain relievers, observation (in some cases)"
    },
    {
        "Code": 238,
        "name": "Myelodysplastic Syndrome",
        "symptoms": "Fatigue, frequent infections, easy bruising or bleeding",
        "treatments": "Supportive care, blood transfusions, medications, bone marrow transplantation (in some cases)"
    },
    {
        "Code": 239,
        "name": "Fracture of the Shoulder",
        "symptoms": "Shoulder pain, swelling, limited range of motion",
        "treatments": "Immobilization (sling, brace), pain management, physical therapy, surgical intervention (in severe cases)"
    },
    {
        "Code": 240,
        "name": "Acute Kidney Injury",
        "symptoms": "Decreased urine output, fluid retention, fatigue",
        "treatments": "Treating underlying cause, supportive care, medications to manage complications, dialysis (in severe cases)"
    },
    {
        "Code": 241,
        "name": "Threatened Pregnancy",
        "symptoms": "Vaginal bleeding, abdominal cramps, pelvic pain",
        "treatments": "Bed rest, medications (progesterone), monitoring, avoiding activities that may stress the pregnancy"
    },
    {
        "Code": 242,
        "name": "Intracranial Abscess",
        "symptoms": "Headache, fever, neurological deficits",
        "treatments": "Antibiotics, surgical drainage or removal of the abscess, supportive care"
    },
    {
        "Code": 243,
        "name": "Gum Disease",
        "symptoms": "Swollen, red, tender gums, bleeding gums",
        "treatments": "Oral hygiene practices (brushing, flossing), professional dental cleanings, medications, surgical interventions"
    },
    {
        "Code": 244,
        "name": "Open Wound from Surgical Incision",
        "symptoms": "Redness, swelling, discharge from the wound",
        "treatments": "Wound care (cleaning, dressing changes), antibiotics (if infection is present), surgical interventions"
    },
    {
        "Code": 245,
        "name": "Gastrointestinal Hemorrhage",
        "symptoms": "Abdominal pain, vomiting blood, bloody or black stools",
        "treatments": "Blood transfusions, endoscopy, surgery (in severe cases), medications to stop bleeding"
    },
    {
        "Code": 246,
        "name": "Seborrheic Dermatitis",
        "symptoms": "Red, itchy, and oily patches of skin, dandruff, flaky scalp",
        "treatments": "Topical antifungal creams or ointments, medicated shampoos, corticosteroid creams"
    },
    {
        "Code": 247,
        "name": "Drug Abuse (Methamphetamine)",
        "symptoms": "Increased energy and alertness, decreased appetite, rapid heartbeat",
        "treatments": "Detoxification, counseling, behavioral therapies, support groups, medication-assisted treatment (if applicable)"
    },
    {
        "Code": 248,
        "name": "Torticollis",
        "symptoms": "Neck pain, stiffness, and abnormal head positioning",
        "treatments": "Physical therapy exercises, pain relievers, botulinum toxin injections (in severe cases)"
    },
    {
        "Code": 249,
        "name": "Antihypertensives Poisoning",
        "symptoms": "Dizziness, low blood pressure, slow heart rate, nausea, vomiting",
        "treatments": "Immediate medical attention, activated charcoal administration, supportive care, specific antidotes"
    },
    {
        "Code": 250,
        "name": "Tension Headache",
        "symptoms": "Mild to moderate head pain, tightness or pressure sensation on both sides of head",
        "treatments": "Over-the-counter pain relievers, relaxation techniques, stress management"
    },
    {
        "Code": 251,
        "name": "Alcohol Intoxication",
        "symptoms": "Slurred speech, impaired coordination, confusion",
        "treatments": "Supportive care, ensuring hydration, monitoring vital signs, prevention of complications"
    },
    {
        "Code": 252,
        "name": "Scurvy",
        "symptoms": "Fatigue, swollen and bleeding gums, joint pain",
        "treatments": "Vitamin C supplementation, dietary changes, oral hygiene maintenance"
    },
    {
        "Code": 253,
        "name": "Narcolepsy",
        "symptoms": "Excessive daytime sleepiness, sudden loss of muscle tone (cataplexy)",
        "treatments": "Stimulant medications, antidepressants, lifestyle modifications, scheduled naps"
    },
    {
        "Code": 254,
        "name": "Food Allergy",
        "symptoms": "Rash, itching, swelling, difficulty breathing, gastrointestinal symptoms",
        "treatments": "Avoidance of allergenic food, antihistamines, epinephrine (in severe cases)"
    },
    {
        "Code": 255,
        "name": "Labyrinthitis",
        "symptoms": "Vertigo, dizziness, nausea, hearing loss, ear pain",
        "treatments": "Medications (antibiotics, antivirals), vestibular rehabilitation therapy"
    },
    {
        "Code": 256,
        "name": "Anxiety",
        "symptoms": "Excessive worrying, restlessness, increased heart rate, panic attacks",
        "treatments": "Therapy (cognitive-behavioral therapy, psychotherapy), medications (antidepressants, anti-anxiety drugs)"
    },
    {
        "Code": 257,
        "name": "Impulse Control Disorder",
        "symptoms": "Impulsive behaviors (e.g., gambling, stealing), difficulty resisting urges",
        "treatments": "Psychotherapy, medication (in some cases), support groups, behavioral interventions"
    },
    {
        "Code": 258,
        "name": "Stenosis of the Tear Duct",
        "symptoms": "Excessive tearing, eye discharge, recurrent eye infections",
        "treatments": "Tear duct probing, dilation, surgical correction"
    },
    {
        "Code": 259,
        "name": "Abscess of Nose",
        "symptoms": "Pain, swelling, redness, discharge from the nose",
        "treatments": "Antibiotics, warm compresses, surgical drainage (in severe cases)"
    },
    {
        "Code": 260,
        "name": "Omphalitis",
        "symptoms": "Redness, swelling, discharge, foul odor around the umbilical area",
        "treatments": "Antibiotics, wound care, surgical intervention (in severe cases)"
    },
    {
        "Code": 261,
        "name": "Leukemia",
        "symptoms": "Fatigue, pale skin, frequent infections, easy bleeding or bruising",
        "treatments": "Chemotherapy, radiation therapy, stem cell transplant, targeted therapy, supportive care"
    },
    {
        "Code": 262,
        "name": "Bell Palsy",
        "symptoms": "Facial weakness or paralysis, drooping of the mouth or eyelid",
        "treatments": "Corticosteroids, antiviral medications, eye protection, physical therapy"
    },
    {
        "Code": 263,
        "name": "Conjunctivitis due to Allergy",
        "symptoms": "Redness, itching, watery discharge, swollen eyelids",
        "treatments": "Allergen avoidance, antihistamine eye drops, cold compresses, lubricating eye drops"
    },
    {
        "Code": 264,
        "name": "Drug Reaction",
        "symptoms": "Rash, itching, swelling, fever, respiratory symptoms",
        "treatments": "Discontinuation of the offending drug, supportive care, antihistamines, corticosteroids (in severe cases)"
    },
    {
        "Code": 265,
        "name": "Adrenal Cancer",
        "symptoms": "Abdominal or back pain, unexplained weight loss, hormonal imbalances",
        "treatments": "Surgery (adrenalectomy), chemotherapy, radiation therapy, targeted therapy, hormone replacement therapy"
    },
    {
        "Code": 266,
        "name": "Myopia",
        "symptoms": "Blurred distance vision, eyestrain, squinting",
        "treatments": "Eyeglasses, contact lenses, refractive surgery (LASIK), orthokeratology (for some cases)"
    },
    {
        "Code": 267,
        "name": "Osteoarthritis",
        "symptoms": "Joint pain, stiffness, swelling",
        "treatments": "Pain relievers, physical therapy, weight management, assistive devices, surgery (in severe cases)"
    },
    {
        "Code": 268,
        "name": "Thyroid Disease",
        "symptoms": "Fatigue, weight changes, mood swings, dry skin",
        "treatments": "Medications (thyroid hormone replacement, antithyroid drugs), radioactive iodine therapy, surgery (in some cases)"
    },
    {
        "Code": 269,
        "name": "Pharyngitis",
        "symptoms": "Sore throat, difficulty swallowing, swollen lymph nodes",
        "treatments": "Rest, pain relievers, throat lozenges, antibiotics (if bacterial infection), symptomatic relief"
    },
    {
        "Code": 270,
        "name": "Chronic Rheumatic Fever",
        "symptoms": "Joint pain, fever, rash, heart inflammation",
        "treatments": "Antibiotics (to treat streptococcal infections), anti-inflammatory medications, medications for heart complications"
    },
    {
        "Code": 271,
        "name": "Hypocalcemia",
        "symptoms": "Numbness or tingling in fingers or around the mouth, muscle cramps",
        "treatments": "Calcium and vitamin D supplements, treating underlying causes, intravenous calcium (in severe cases)"
    },
    {
        "Code": 272,
        "name": "Macular Degeneration",
        "symptoms": "Blurred or distorted central vision, blind spots",
        "treatments": "Vision aids, medications (injections into the eye), laser therapy, photodynamic therapy, surgical intervention"
    },
    {
        "Code": 273,
        "name": "Pneumonia",
        "symptoms": "Cough, fever, chest pain, difficulty breathing",
        "treatments": "Antibiotics, antiviral medications (if applicable), rest, fluids, symptomatic relief"
    },
    {
        "Code": 274,
        "name": "Cold Sore",
        "symptoms": "Small, painful blisters on the lips or around the mouth",
        "treatments": "Antiviral medications (topical or oral), pain relievers, antiviral creams, self-care measures"
    },
    {
        "Code": 275,
        "name": "Premature Ventricular Contractions (PVCs)",
        "symptoms": "Skipped or extra heartbeats, palpitations, lightheadedness",
        "treatments": "Monitoring (in most cases), lifestyle changes, medications (beta-blockers, antiarrhythmics)"
    },
    {
        "Code": 276,
        "name": "Chancroid",
        "symptoms": "Painful ulcers or sores on the genital area, swollen lymph nodes in the groin",
        "treatments": "Antibiotics (such as azithromycin or ceftriaxone), pain management, warm compresses, good hygiene"
    },
    {
        "Code": 277,
        "name": "Testicular Cancer",
        "symptoms": "Lump or swelling in the testicles, pain or discomfort, changes in testicular size or shape",
        "treatments": "Surgery (orchiectomy), chemotherapy, radiation therapy, surveillance (for some cases)"
    },
    {
        "Code": 278,
        "name": "Hydrocephalus",
        "symptoms": "Headache, nausea, vomiting, cognitive or developmental problems, enlarged head in infants",
        "treatments": "Shunt placement (to divert excess cerebrospinal fluid), endoscopic third ventriculostomy, medication (in some cases)"
    },
    {
        "Code": 279,
        "name": "Breast Cancer",
        "symptoms": "Breast lump, changes in breast size or shape, nipple changes, breast pain",
        "treatments": "Surgery (lumpectomy or mastectomy), radiation therapy, chemotherapy, hormone therapy, targeted therapy"
    },
    {
        "Code": 280,
        "name": "Anemia due to Malignancy",
        "symptoms": "Fatigue, weakness, shortness of breath, pale skin",
        "treatments": "Treating underlying malignancy, blood transfusions, medications (erythropoiesis-stimulating agents, iron supplements)"
    },
    {
        "Code": 281,
        "name": "Esophageal Varices",
        "symptoms": "Swollen blood vessels in the esophagus, vomiting blood, black, tarry stools",
        "treatments": "Medications (beta-blockers, vasoconstrictors), endoscopic therapies, band ligation, transjugular intrahepatic portosystemic shunt (TIPS), surgical interventions"
    },
    {
        "Code": 282,
        "name": "Endometrial Cancer",
        "symptoms": "Abnormal vaginal bleeding, pelvic pain or discomfort, changes in bowel or bladder habits",
        "treatments": "Surgery (hysterectomy), radiation therapy, chemotherapy, hormone therapy"
    },
    {
        "Code": 283,
        "name": "Cystic Fibrosis",
        "symptoms": "Persistent cough with thick mucus, recurrent lung infections, poor growth or weight gain, salty-tasting skin",
        "treatments": "Medications (mucus-thinning drugs, bronchodilators), chest physical therapy, enzyme supplements, lung transplant (in severe cases)"
    },
    {
        "Code": 284,
        "name": "Intertrigo",
        "symptoms": "Red, raw, or inflamed skin in skin folds (such as armpits or groin), itching or burning sensation",
        "treatments": "Keeping the affected area clean and dry, applying topical antifungal or antibacterial creams, using barrier creams"
    },
    {
        "Code": 285,
        "name": "Parathyroid Adenoma",
        "symptoms": "Fatigue, weakness, bone pain, frequent urination, kidney stones",
        "treatments": "Surgical removal of the adenoma (parathyroidectomy), medications to manage calcium levels"
    },
    {
        "Code": 286,
        "name": "Glucocorticoid Deficiency",
        "symptoms": "Fatigue, weakness, weight loss, low blood pressure, abdominal pain",
        "treatments": "Hormone replacement therapy with glucocorticoid medications"
    },
    {
        "Code": 287,
        "name": "Temporomandibular Joint Disorder",
        "symptoms": "Jaw pain or tenderness, clicking or popping sounds in the jaw joint, difficulty chewing or opening the mouth",
        "treatments": "Self-care measures (rest, applying heat or cold, jaw exercises), pain medications, physical therapy, oral splints"
    },
    {
        "Code": 288,
        "name": "Wilson Disease",
        "symptoms": "Fatigue, abdominal pain or swelling, jaundice, neurological symptoms (tremors, difficulty speaking or walking)",
        "treatments": "Medications to remove copper from the body (chelators), dietary changes, liver transplant (in severe cases)"
    },
    {
        "Code": 289,
        "name": "Vesicoureteral Reflux",
        "symptoms": "Frequent urinary tract infections, urinary urgency or frequency, bedwetting (in children), high blood pressure (in severe cases)",
        "treatments": "Antibiotics, bladder training exercises, surgical correction (in some cases)"
    },
    {
        "Code": 290,
        "name": "Vitamin A Deficiency",
        "symptoms": "Night blindness, dry eyes, dry or rough skin, poor wound healing, weakened immune system",
        "treatments": "Vitamin A supplementation, dietary changes to include foods rich in vitamin A"
    },
    {
        "Code": 291,
        "name": "Gonorrhea",
        "symptoms": "Painful urination, abnormal discharge from the genitals, pelvic pain",
        "treatments": "Antibiotics (dual therapy with ceftriaxone and azithromycin), safe sexual practices, partner notification"
    },
    {
        "Code": 292,
        "name": "Fracture of the Rib",
        "symptoms": "Chest pain, difficulty breathing, tenderness or swelling over the ribcage",
        "treatments": "Pain management, rest, immobilization (splinting or bracing), physical therapy"
    },
    {
        "Code": 293,
        "name": "Ependymoma",
        "symptoms": "Headaches, nausea, seizures, changes in coordination or balance",
        "treatments": "Surgery, radiation therapy, chemotherapy, targeted therapy, rehabilitation"
    },
    {
        "Code": 294,
        "name": "Hepatitis due to a Toxin",
        "symptoms": "Fatigue, jaundice, abdominal pain, nausea, vomiting",
        "treatments": "Supportive care, removal or avoidance of the toxic substance, management of symptoms"
    },
    {
        "Code": 295,
        "name": "Vaginal Cyst",
        "symptoms": "Small lump or swelling in the vaginal wall, discomfort or pain during intercourse",
        "treatments": "Observation (if asymptomatic), warm compresses, sitz baths, surgical removal (if necessary)"
    },
    {
        "Code": 296,
        "name": "Chronic Knee Pain",
        "symptoms": "Persistent knee pain, stiffness, swelling, limited range of motion",
        "treatments": "Pain management, physical therapy, lifestyle modifications, knee braces or supports"
    },
    {
        "Code": 297,
        "name": "Pinguecula",
        "symptoms": "Yellowish or white growth on the conjunctiva (eye's surface), usually near the cornea",
        "treatments": "Artificial tears, lubricating eye drops, sunglasses for UV protection, surgical removal (in severe cases)"
    },
    {
        "Code": 298,
        "name": "Hypergammaglobulinemia",
        "symptoms": "Elevated levels of gamma globulins in the blood, may be asymptomatic or associated with other underlying conditions",
        "treatments": "Treatment of underlying cause or associated condition, immunosuppressive therapy (in some cases)"
    },
    {
        "Code": 299,
        "name": "Pituitary Disorder",
        "symptoms": "Various symptoms depending on the specific disorder, including hormonal imbalances",
        "treatments": "Treatment depends on the specific pituitary disorder and may involve medications, surgery, hormone replacement therapy"
    },
    {
        "Code": 300,
        "name": "Kidney Stone",
        "symptoms": "Severe pain in the side or back, blood in the urine, frequent urination",
        "treatments": "Pain management, increased fluid intake, medication to facilitate stone passage, minimally invasive procedures or surgery"
    },
    {
        "Code": 301,
        "name": "Autism",
        "symptoms": "Challenges with social interaction, communication difficulties, restricted interests or repetitive behaviors",
        "treatments": "Behavioral therapy, educational interventions, speech and language therapy, medications for associated symptoms"
    },
    {
        "Code": 302,
        "name": "Cat Scratch Disease",
        "symptoms": "Swollen lymph nodes, fever, fatigue, headache, rash",
        "treatments": "Antibiotics (azithromycin, doxycycline), pain management, supportive care"
    },
    {
        "Code": 303,
        "name": "Chronic Glaucoma",
        "symptoms": "Gradual vision loss, peripheral vision impairment, eye pain or discomfort, halos around lights",
        "treatments": "Eye drops (to reduce intraocular pressure), oral medications, laser therapy, surgery (trabeculectomy, implantable devices), regular eye exams"
    },
    {
        "Code": 304,
        "name": "Retinal Detachment",
        "symptoms": "Floaters (spots or cobweb-like shapes in vision), flashes of light, curtain-like shadow over vision, sudden vision loss",
        "treatments": "Surgical intervention (pneumatic retinopexy, scleral buckle, vitrectomy), laser therapy, cryotherapy, gas or silicone oil injection, positioning, regular eye exams"
    },
    {
        "Code": 305,
        "name": "Aplastic Anemia",
        "symptoms": "Fatigue, pale skin, frequent infections, shortness of breath, rapid or irregular heartbeats, prolonged bleeding or bruising",
        "treatments": "Blood transfusions, bone marrow-stimulating medications, immunosuppressive therapy, stem cell transplant (in severe cases), supportive care"
    },
    {
        "Code": 306,
        "name": "Overflow Incontinence",
        "symptoms": "Frequent or constant dribbling of urine, inability to completely empty the bladder, weak urine stream",
        "treatments": "Bladder training exercises, double voiding, catheterization, medications (alpha-blockers, anticholinergics), surgery (in severe cases), lifestyle modifications"
    },
    {
        "Code": 307,
        "name": "Rabies",
        "symptoms": "Flu-like symptoms (fever, headache, fatigue), anxiety, confusion, hallucinations, difficulty swallowing",
        "treatments": "Immediate medical attention (post-exposure prophylaxis), wound care, administration of rabies vaccine and immunoglobulin, supportive care, monitoring and management of symptoms"
    },
    {
        "Code": 308,
        "name": "Hemolytic Anemia",
        "symptoms": "Fatigue, weakness, pale skin, shortness of breath, jaundice",
        "treatments": "Treatment of underlying cause, blood transfusions, medications (immunosuppressants, corticosteroids), splenectomy (in some cases), supportive care, folic acid or iron supplementation"
    },
    {
        "Code": 309,
        "name": "Lateral Epicondylitis (Tennis Elbow)",
        "symptoms": "Pain or tenderness on the outer side of the elbow, weak grip strength, difficulty with forearm movements",
        "treatments": "Rest, ice or cold therapy, compression, elbow brace or strap, pain relievers, physical therapy exercises, corticosteroid injections (in severe cases), ergonomic modifications"
    },
    {
        "Code": 310,
        "name": "Syphilis",
        "symptoms": "Primary stage: painless sores (chancre) at the site of infection, secondary stage: skin rash, fever, swollen lymph nodes, sore throat, latent stage: no symptoms, tertiary stage: severe complications affecting the heart, brain, and other organs",
        "treatments": "Antibiotics (usually penicillin), treatment of complications, regular follow-up and testing"
    },
    {
        "Code": 311,
        "name": "Diabetic Kidney Disease",
        "symptoms": "High blood pressure, increased need to urinate, swelling in the legs and ankles, fatigue, nausea, loss of appetite",
        "treatments": "Blood pressure control, blood sugar control, medications to protect the kidneys (such as ACE inhibitors or ARBs), lifestyle modifications (healthy diet, regular exercise, quitting smoking), management of underlying diabetes, treatment of complications (such as dialysis or kidney transplantation in advanced stages)"
    },
    {
        "Code": 312,
        "name": "Nose Disorder",
        "symptoms": "Nasal congestion, runny nose, sneezing, facial pain or pressure, loss of smell",
        "treatments": "Treatment depends on the underlying cause (such as allergies, sinusitis, or nasal polyps), and may include medications (such as decongestants, antihistamines, nasal sprays), saline nasal irrigation, steam inhalation, allergy management, antibiotics (if bacterial infection is present), surgical intervention (in some cases)"
    },
    {
        "Code": 313,
        "name": "Drug Withdrawal",
        "symptoms": "Anxiety, restlessness, irritability, tremors, sweating, nausea, vomiting, insomnia, drug cravings",
        "treatments": "Gradual tapering of the drug under medical supervision, medications to manage withdrawal symptoms (such as benzodiazepines, clonidine, or buprenorphine), behavioral therapy, support groups, counseling, rehabilitation programs"
    },
    {
        "Code": 314,
        "name": "Dental Caries",
        "symptoms": "Toothache, tooth sensitivity, visible pits or holes in the teeth, dark spots on the teeth, bad breath",
        "treatments": "Dental fillings, crowns, root canal treatment, tooth extraction (in severe cases), oral hygiene practices (brushing and flossing), regular dental check-ups, fluoride treatments, dietary modifications (reducing sugary and acidic foods and drinks), dental sealants (for prevention), education on proper oral care"
    },
    {
        "Code": 315,
        "name": "Hypercholesterolemia",
        "symptoms": "High levels of cholesterol in the blood, fatty deposits (xanthomas) on the skin or tendons, chest pain or angina, heart attacks, strokes",
        "treatments": "Lifestyle modifications (healthy diet, regular exercise, weight management, smoking cessation), medications to lower cholesterol levels (such as statins), regular monitoring of cholesterol levels, management of underlying conditions (such as diabetes or high blood pressure), potential additional treatments (such as bile acid sequestrants or PCSK9 inhibitors)"
    },
    {
        "Code": 316,
        "name": "Fracture of the Patella",
        "symptoms": "Severe pain, swelling, bruising, difficulty straightening or bending the knee, deformity",
        "treatments": "Immobilization (splint, cast, or brace), pain management, physical therapy, exercises to restore mobility and strength, potential surgical intervention (in severe cases or if displacement is present)"
    },
    {
        "Code": 317,
        "name": "Kidney Failure",
        "symptoms": "Decreased urine output, fluid retention, fatigue, shortness of breath, nausea, confusion, chest pain, seizures",
        "treatments": "Treatment depends on the underlying cause and may include medications to manage blood pressure and symptoms, dietary modifications (restricting salt, protein, and potassium), dialysis (hemodialysis or peritoneal dialysis) or kidney transplantation (in end-stage kidney failure), treatment of complications, management of fluid and electrolyte balance, lifestyle modifications (exercise, quitting smoking, healthy diet)"
    },
    {
        "Code": 318,
        "name": "Fracture of the Neck",
        "symptoms": "Severe neck pain, swelling, tenderness, difficulty moving or turning the head, numbness or weakness in the arms or legs",
        "treatments": "Immobilization (cervical collar, brace), pain management, potential surgical intervention (in severe cases)"
    },
    {
        "Code": 319,
        "name": "Muscle Spasm",
        "symptoms": "Sudden, involuntary muscle contractions, muscle pain, stiffness, limited range of motion",
        "treatments": "Stretching and relaxation exercises, heat or cold therapy, over-the-counter pain relievers, muscle relaxants, physical therapy, lifestyle modifications"
    },
    {
        "Code": 320,
        "name": "Hemophilia",
        "symptoms": "Excessive bleeding and bruising, prolonged bleeding from wounds or after dental work or surgery, spontaneous bleeding in joints or muscles",
        "treatments": "Replacement therapy with clotting factor concentrates, medications to control bleeding, physical therapy, joint protection measures, genetic counseling and testing for family members"
    },
    {
        "Code": 321,
        "name": "Hyperosmotic Hyperketotic State",
        "symptoms": "Increased blood sugar levels, increased ketone production, excessive thirst, frequent urination, fatigue, confusion, fruity breath odor",
        "treatments": "Insulin therapy to regulate blood sugar levels, intravenous fluids to correct dehydration, electrolyte replacement, correction of underlying causes (e.g., diabetes management)"
    },
    {
        "Code": 322,
        "name": "Peritonsillar Abscess",
        "symptoms": "Severe sore throat, difficulty swallowing, fever, swollen tonsils, voice changes, neck pain or stiffness",
        "treatments": "Antibiotics to treat infection, drainage of the abscess (needle aspiration or incision and drainage), pain relievers, warm saltwater gargles, rest, fluids, surgical removal of the tonsils (in chronic or recurrent cases)"
    },
    {
        "Code": 323,
        "name": "Gastroparesis",
        "symptoms": "Nausea, vomiting, early satiety, bloating, abdominal pain, poor appetite",
        "treatments": "Dietary modifications (small, frequent meals; low-fiber, low-fat diet), medication to promote gastric emptying, managing underlying cause if possible"
    },
    {
        "Code": 324,
        "name": "Fat Embolism",
        "symptoms": "Respiratory distress, chest pain, confusion, petechial rash (small red or purple spots), neurological symptoms",
        "treatments": "Supportive care (oxygen therapy, fluid resuscitation), managing symptoms (pain medication, anticoagulants), treatment of underlying cause if possible"
    },
    {
        "Code": 325,
        "name": "Polycythemia Vera",
        "symptoms": "Increased red blood cell count, fatigue, headache, dizziness, itching, enlarged spleen",
        "treatments": "Phlebotomy (removal of blood), medication (hydroxyurea, interferon), low-dose aspirin, managing complications (blood thinners, medication for itching)"
    },
    {
        "Code": 326,
        "name": "Thrombocytopenia",
        "symptoms": "Easy bruising, prolonged bleeding from cuts, petechiae (red or purple spots on the skin), nosebleeds, excessive menstrual bleeding",
        "treatments": "Treatment of underlying cause, platelet transfusion (if severe), medication (corticosteroids, immunosuppressants), avoiding medications that can worsen platelet counts"
    },
    {
        "Code": 327,
        "name": "Head and Neck Cancer",
        "symptoms": "Persistent sore throat, difficulty swallowing, voice changes, ear pain, neck mass, weight loss",
        "treatments": "Treatment depends on the specific type and stage of cancer, and may include surgery, radiation therapy, chemotherapy, targeted therapy, immunotherapy"
    },
    {
        "Code": 328,
        "name": "Pseudohypoparathyroidism",
        "symptoms": "Hypocalcemia (low calcium levels), tetany (muscle spasms), short stature, rounded face",
        "treatments": "Calcium and vitamin D supplementation, management of complications, hormone replacement therapy (if necessary)"
    },
    {
        "Code": 329,
        "name": "Goiter",
        "symptoms": "Enlarged thyroid gland in the neck, swelling or visible protrusion, difficulty swallowing or breathing",
        "treatments": "Treatment depends on the underlying cause (medication, radioactive iodine therapy, surgery)"
    },
    {
        "Code": 330,
        "name": "Urge Incontinence",
        "symptoms": "Sudden, intense urge to urinate followed by involuntary urine leakage",
        "treatments": "Behavioral therapies (bladder training, pelvic floor exercises), medications (anticholinergics, beta-3 agonists), medical devices"
    },
    {
        "Code": 331,
        "name": "Edward Syndrome",
        "symptoms": "Developmental delays, intellectual disability, distinct facial features (small jaw, low-set ears), heart defects",
        "treatments": "Supportive care, addressing associated medical issues, early intervention programs, palliative care"
    },
    {
        "Code": 332,
        "name": "Muscular Dystrophy",
        "symptoms": "Progressive muscle weakness and degeneration, difficulty walking or moving, muscle wasting",
        "treatments": "Supportive care, physical therapy, assistive devices, medications for symptom management, gene therapies (in some cases)"
    },
    {
        "Code": 333,
        "name": "Mittelschmerz",
        "symptoms": "Lower abdominal pain and discomfort occurring around the time of ovulation",
        "treatments": "Pain management (over-the-counter pain relievers, heat therapy), hormonal birth control (if severe or recurrent)"
    },
    {
        "Code": 334,
        "name": "Corneal Abrasion",
        "symptoms": "Eye pain, redness, foreign body sensation, sensitivity to light",
        "treatments": "Eye patching, lubricating eye drops, antibiotic ointments (if infected), avoiding further eye irritation"
    },
    {
        "Code": 335,
        "name": "Anemia of Chronic Disease",
        "symptoms": "Fatigue, weakness, pale skin, shortness of breath, decreased exercise tolerance",
        "treatments": "Treating the underlying chronic disease, addressing nutritional deficiencies, blood transfusions (in severe cases)"
    },
    {
        "Code": 336,
        "name": "Dysthymic Disorder",
        "symptoms": "Persistent depressive symptoms (low mood, lack of interest, changes in sleep and appetite), lasting for at least two years",
        "treatments": "Psychotherapy (cognitive-behavioral therapy, interpersonal therapy), antidepressant medications"
    },
    {
        "Code": 337,
        "name": "Scarlet Fever",
        "symptoms": "Sore throat, fever, rash (red, sandpaper-like), swollen glands",
        "treatments": "Antibiotics (such as penicillin or erythromycin), rest, fluids, symptomatic relief"
    },
    {
        "Code": 338,
        "name": "Hypertensive Heart Disease",
        "symptoms": "High blood pressure, chest pain or discomfort, shortness of breath, fatigue",
        "treatments": "Medications (antihypertensives), lifestyle changes (healthy diet, exercise, stress management), treatment of underlying conditions"
    },
    {
        "Code": 339,
        "name": "Drug Abuse (Barbiturates)",
        "symptoms": "Sedation, drowsiness, slurred speech, confusion, respiratory depression",
        "treatments": "Medical detoxification, supportive care, counseling, rehabilitation programs"
    },
    {
        "Code": 340,
        "name": "Polycystic Ovarian Syndrome",
        "symptoms": "Irregular periods, excessive hair growth, acne, weight gain, ovarian cysts",
        "treatments": "Lifestyle changes (diet, exercise, weight management), hormonal contraceptives, fertility treatments (if needed)"
    },
    {
        "Code": 341,
        "name": "Encephalitis",
        "symptoms": "Headache, fever, confusion, seizures, neurological symptoms",
        "treatments": "Hospitalization, antiviral medications (if caused by a viral infection), supportive care"
    },
    {
        "Code": 342,
        "name": "Cyst of the Eyelid",
        "symptoms": "Painful lump or swelling on the eyelid, redness, tenderness",
        "treatments": "Warm compresses, good eyelid hygiene, antibiotic ointments (if infected), surgical removal (if necessary)"
    },
    {
        "Code": 343,
        "name": "Balanitis",
        "symptoms": "Inflammation of the glans penis (tip of the penis), redness, swelling, pain",
        "treatments": "Good hygiene, topical antifungal or antibacterial creams, corticosteroid creams (if severe), treating underlying causes"
    },
    {
        "Code": 344,
        "name": "Foreign Body in the Throat",
        "symptoms": "Sensation of a foreign object stuck in the throat, difficulty swallowing or speaking",
        "treatments": "Immediate medical attention, removal of the foreign body, evaluation for any complications"
    },
    {
        "Code": 345,
        "name": "Drug Abuse (Cocaine)",
        "symptoms": "Euphoria, increased energy, dilated pupils, rapid heart rate, high blood pressure, risk of heart attack or stroke",
        "treatments": "Medical detoxification, counseling, behavioral therapies, support groups"
    },
    {
        "Code": 346,
        "name": "Optic Neuritis",
        "symptoms": "Vision loss or blurry vision, eye pain with eye movement, color vision impairment, flashing lights or floaters",
        "treatments": "High-dose intravenous corticosteroids, treatment of underlying cause, symptom management, visual rehabilitation"
    },
    {
        "Code": 347,
        "name": "Intestinal Malabsorption",
        "symptoms": "Chronic diarrhea, weight loss, abdominal pain or bloating, nutrient deficiencies (vitamins, minerals), fatigue, failure to thrive",
        "treatments": "Dietary modifications (specific to the underlying cause), supplementation of deficient nutrients, medications (to manage symptoms or underlying condition), treatment of underlying cause"
    },
    {
        "Code": 348,
        "name": "Lead Poisoning",
        "symptoms": "Fatigue, abdominal pain, joint pain, memory loss or cognitive difficulties, developmental delays (in children), anemia",
        "treatments": "Removal of lead source, chelation therapy (in severe cases), supportive care, medication to manage symptoms, addressing complications (such as anemia)"
    },
    {
        "Code": 349,
        "name": "Viral Warts",
        "symptoms": "Small, rough growths on the skin or mucous membranes, typically painless, may appear in clusters or as single lesions",
        "treatments": "Topical treatments (salicylic acid, cryotherapy), laser therapy, surgical removal, immune therapy (for persistent or recurrent cases)"
    },
    {
        "Code": 350,
        "name": "Hyperhidrosis",
        "symptoms": "Excessive sweating (beyond what is necessary for temperature regulation), typically in specific areas (such as palms, soles, underarms), may interfere with daily activities",
        "treatments": "Antiperspirants, medications (anticholinergics, beta blockers), iontophoresis, Botox injections, surgical interventions (sympathectomy, sweat gland removal)"
    },
    {
        "Code": 351,
        "name": "Stroke",
        "symptoms": "Sudden numbness or weakness of the face, arm, or leg (typically on one side of the body), confusion, trouble speaking or understanding, severe headache",
        "treatments": "Emergency medical attention, medication (clot-busting drugs, anticoagulants), supportive care, rehabilitation (physical therapy, speech therapy), lifestyle modifications (diet, exercise, smoking cessation), addressing underlying risk factors"
    },
    {
        "Code": 352,
        "name": "Pilonidal Cyst",
        "symptoms": "Pain or discomfort in the tailbone area, swelling, redness, drainage of pus or blood, abscess formation",
        "treatments": "Warm compresses, pain management, antibiotics (for infection), incision and drainage, surgical removal or excision, wound care, lifestyle modifications to prevent recurrence"
    },
    {
        "Code": 353,
        "name": "Crushing Injury",
        "symptoms": "Severe pain, swelling, deformity, bruising, difficulty moving or using the affected area",
        "treatments": "Emergency medical attention, immobilization, pain management, surgery (to repair or reconstruct affected tissues), rehabilitation (physical therapy, occupational therapy)"
    },
    {
        "Code": 354,
        "name": "Normal Pressure Hydrocephalus",
        "symptoms": "Gait disturbances, urinary incontinence, cognitive decline or dementia-like symptoms",
        "treatments": "Ventriculoperitoneal shunt placement, medication management for symptoms"
    },
    {
        "Code": 355,
        "name": "Alopecia",
        "symptoms": "Hair loss or balding, patchy or generalized hair loss",
        "treatments": "Topical medications (minoxidil), oral medications (finasteride), steroid injections, hair transplant surgery, wigs or hairpieces"
    },
    {
        "Code": 356,
        "name": "Hashimoto Thyroiditis",
        "symptoms": "Fatigue, weight gain, constipation, dry skin, depression, muscle aches and stiffness, sensitivity to cold",
        "treatments": "Thyroid hormone replacement (levothyroxine), monitoring and management of symptoms"
    },
    {
        "Code": 357,
        "name": "Flat Feet",
        "symptoms": "Foot pain or achiness, difficulty with foot and ankle movement, foot fatigue, swelling",
        "treatments": "Supportive footwear, orthotic inserts, physical therapy exercises, pain management, surgery (in severe cases)"
    },
    {
        "Code": 358,
        "name": "Nonalcoholic Liver Disease (NASH)",
        "symptoms": "Fatigue, abdominal swelling or pain, enlarged liver, elevated liver enzymes, insulin resistance",
        "treatments": "Lifestyle changes (weight loss, healthy diet, regular exercise), management of underlying conditions, medication as needed"
    },
    {
        "Code": 359,
        "name": "Hemarthrosis",
        "symptoms": "Joint swelling, pain, warmth, limited range of motion",
        "treatments": "RICE method (Rest, Ice, Compression, Elevation), pain management, joint aspiration or drainage (in severe cases)"
    },
    {
        "Code": 360,
        "name": "Pelvic Organ Prolapse",
        "symptoms": "Pelvic pressure or heaviness, urinary incontinence, bowel movement difficulties, discomfort or pain during intercourse",
        "treatments": "Pelvic floor exercises, pessary use, hormone therapy, surgical repair (in severe cases)"
    },
    {
        "Code": 361,
        "name": "Fracture of the Arm",
        "symptoms": "Pain, swelling, deformity, limited mobility or difficulty moving the arm, bruising",
        "treatments": "Immobilization (cast or splint), pain management, physical therapy, surgery (in complex fractures)"
    },
    {
        "Code": 362,
        "name": "Coagulation (Bleeding) Disorder",
        "symptoms": "Easy bruising, prolonged bleeding after injury or surgery, excessive bleeding from minor cuts or abrasions, frequent nosebleeds, heavy menstrual bleeding",
        "treatments": "Blood transfusions, clotting factor replacement therapy, medications to stimulate clotting, lifestyle modifications, surgery (in some cases)"
    },
    {
        "Code": 363,
        "name": "Intracranial Hemorrhage",
        "symptoms": "Severe headache, nausea or vomiting, changes in vision, loss of consciousness, seizures",
        "treatments": "Emergency medical attention, surgery (if needed), medications to control bleeding and manage symptoms"
    },
    {
        "Code": 364,
        "name": "Hyperkalemia",
        "symptoms": "Muscle weakness or fatigue, irregular heartbeat or palpitations, numbness or tingling, nausea or vomiting",
        "treatments": "Treatment of underlying cause, medications to reduce potassium levels, dietary modifications, dialysis (in severe cases)"
    },
    {
        "Code": 365,
        "name": "Cornea Infection",
        "symptoms": "Eye redness, pain or discomfort, blurred or decreased vision, increased sensitivity to light",
        "treatments": "Antibiotic or antifungal eye drops, oral medications, supportive care, possible corneal transplant (in severe cases)"
    },
    {
        "Code": 366,
        "name": "Abscess of the Lung",
        "symptoms": "Cough with phlegm or pus, chest pain, fever, shortness of breath, fatigue",
        "treatments": "Antibiotics, drainage or surgical removal of the abscess, supportive care, management of underlying lung conditions"
    },
    {
        "Code": 367,
        "name": "Dengue Fever",
        "symptoms": "High fever, severe headache, joint and muscle pain, rash, nausea or vomiting, bleeding tendencies",
        "treatments": "Supportive care (hydration, pain relievers, rest), monitoring, medical attention for severe cases (fluid replacement, blood transfusion, hospitalization)"
    },
    {
        "Code": 368,
        "name": "Chronic Sinusitis",
        "symptoms": "Facial pain or pressure, nasal congestion, thick nasal discharge, postnasal drip, cough, fatigue",
        "treatments": "Saline nasal irrigation, nasal corticosteroids, antibiotics (in bacterial cases), decongestants, pain relievers, surgery (in severe or chronic cases)"
    },
    {
        "Code": 369,
        "name": "Cholesteatoma",
        "symptoms": "Ear pain, hearing loss, ear drainage, dizziness or vertigo, tinnitus",
        "treatments": "Surgical removal, antibiotics (for associated infections)"
    },
    {
        "Code": 370,
        "name": "Volvulus",
        "symptoms": "Abdominal pain, nausea, vomiting, bloating, constipation, bloody stool",
        "treatments": "Emergency surgery to untwist the affected organ and restore blood flow"
    },
    {
        "Code": 371,
        "name": "Injury to the Finger",
        "symptoms": "Pain, swelling, bruising, deformity, restricted range of motion, difficulty gripping or using the finger",
        "treatments": "RICE method (Rest, Ice, Compression, Elevation), splinting, pain medication, physical therapy, surgery (in severe cases)"
    },
    {
        "Code": 372,
        "name": "Poisoning due to Analgesics",
        "symptoms": "Nausea, vomiting, abdominal pain, liver or kidney damage, dizziness, confusion, respiratory distress",
        "treatments": "Immediate medical attention, activated charcoal administration, supportive care, antidote (if available), treatment for complications"
    },
    {
        "Code": 373,
        "name": "Atrial Fibrillation",
        "symptoms": "Irregular or rapid heartbeat, palpitations, shortness of breath, chest pain or discomfort, dizziness or lightheadedness, fatigue",
        "treatments": "Medications (antiarrhythmics, anticoagulants), electrical cardioversion, catheter ablation, lifestyle changes"
    },
    {
        "Code": 374,
        "name": "Pinworm Infection",
        "symptoms": "Itching around the anus or vagina, restless sleep, irritability, anal or vaginal discharge, abdominal pain or discomfort, loss of appetite",
        "treatments": "Anthelmintic medication, hygiene measures (handwashing, trimming nails, laundering bedding), treatment for household members"
    },
    {
        "Code": 375,
        "name": "Urethral Valves",
        "symptoms": "Difficulty or poor urinary stream, urinary tract infections, urinary frequency or urgency, abdominal distension, poor weight gain",
        "treatments": "Surgical intervention (valve ablation or resection), catheterization, medications for symptoms and complications"
    },
    {
        "Code": 376,
        "name": "Migraine",
        "symptoms": "Severe headaches, nausea, sensitivity to light and sound",
        "treatments": "Pain-relieving medications, lifestyle changes, preventive medications"
    },
    {
        "Code": 377,
        "name": "Arthritis",
        "symptoms": "Joint pain, stiffness, swelling",
        "treatments": "Medications, physical therapy, surgery (in severe cases)"
    },
    {
        "Code": 378,
        "name": "Sciatica",
        "symptoms": "Lower back pain, leg pain, numbness or tingling",
        "treatments": "Pain relievers, physical therapy, exercise"
    },
    {
        "Code": 379,
        "name": "Complex Regional Pain Syndrome (CRPS)",
        "symptoms": "Intense burning pain, swelling, changes in skin temperature",
        "treatments": "Physical therapy, medications, nerve blocks"
    },
    {
        "Code": 380,
        "name": "Lupus",
        "symptoms": "Joint pain, fatigue, skin rashes",
        "treatments": "Medications (anti-inflammatory, immunosuppressants), lifestyle modifications"
    },
    {
        "Code": 381,
        "name": "Endometriosis",
        "symptoms": "Pelvic pain, painful periods, infertility",
        "treatments": "Pain medications, hormonal therapies, surgery"
    },
    {
        "Code": 382,
        "name": "Chronic Headache",
        "symptoms": "Persistent head pain, tension in neck and shoulders",
        "treatments": "Pain-relieving medications, relaxation techniques, stress management"
    },
    {
        "Code": 383,
        "name": "Dry Skin",
        "symptoms": "Dry, flaky skin with itching",
        "treatments": "Moisturizing creams or lotions, avoiding hot showers or baths, using mild soaps"
    },
    {
        "Code": 384,
        "name": "Eczema",
        "symptoms": "Itchy, red, inflamed skin, rash",
        "treatments": "Emollients (moisturizers), topical corticosteroids or immunomodulators, avoiding triggers"
    },
    {
        "Code": 385,
        "name": "Psoriasis",
        "symptoms": "Red, scaly patches on the skin, itching",
        "treatments": "Topical treatments (corticosteroids, salicylic acid), systemic medications (retinoids, immunosuppressants), phototherapy"
    },
    {
        "Code": 386,
        "name": "Scabies",
        "symptoms": "Intense itching, especially at night, small blisters or bumps",
        "treatments": "Prescription medications (topical or oral scabicides), washing clothes and bedding in hot water, vacuuming and cleaning home"
    },
    {
        "Code": 387,
        "name": "Urticaria (Hives)",
        "symptoms": "Raised, itchy welts on the skin",
        "treatments": "Antihistamines, avoiding triggers, corticosteroids (in severe cases)"
    },
    {
        "Code": 388,
        "name": "Insect Bites",
        "symptoms": "Red, swollen, itchy bumps",
        "treatments": "Topical corticosteroids, oral antihistamines, cold compresses"
    },
    {
        "Code": 389,
        "name": "Contact Dermatitis",
        "symptoms": "Itchy, red rash caused by contact with irritants or allergens",
        "treatments": "Avoiding the trigger, corticosteroid creams or ointments, antihistamines"
    },
    {
        "Code": 390,
        "name": "Dermatitis due to Sun Exposure",
        "symptoms": "Sunburn-like rash, redness, itching",
        "treatments": "Moisturizers, cool compresses, topical corticosteroids"
    },
    {
        "Code": 391,
        "name": "Parasitic Infections",
        "symptoms": "Intense itching, visible lice or nits in the affected area",
        "treatments": "Prescription medications (topical or oral antiparasitic agents), washing clothes and bedding in hot water"
    },
    {
        "Code": 392,
        "name": "Influenza (Flu)",
        "symptoms": "High fever, body aches, fatigue, cough, sore throat, congestion",
        "treatments": "Rest, fluids, over-the-counter medications for symptom relief, antiviral medications (in some cases)"
    },
    {
        "Code": 393,
        "name": "Urinary Tract Infection (UTI)",
        "symptoms": "Frequent urination, burning sensation during urination, cloudy or bloody urine, pelvic pain",
        "treatments": "Antibiotics, increased fluid intake, pain relievers"
    },
    {
        "Code": 394,
        "name": "Bronchitis",
        "symptoms": "Persistent cough with yellow or green mucus, chest congestion, fatigue",
        "treatments": "Rest, fluids, over-the-counter cough suppressants, inhalers (if prescribed), treating underlying cause"
    },
    {
        "Code": 395,
        "name": "Gastroenteritis (Stomach Flu)",
        "symptoms": "Nausea, vomiting, diarrhea, abdominal pain or cramps, fever",
        "treatments": "Rest, fluids (electrolyte solutions), bland diet, avoiding irritating foods, over-the-counter medications for symptom relief"
    },
    {
        "Code": 396,
        "name": "Urinary Stones (Kidney Stones)",
        "symptoms": "Severe abdominal or back pain, blood in urine, frequent urination, pain during urination",
        "treatments": "Pain management, increased fluid intake, medications to help pass the stones, procedures or surgery"
    },
    {
        "Code": 397,
        "name": "Osteoporosis",
        "symptoms": "Fragile bones, loss of height over time, back pain, fractures",
        "treatments": "Calcium and vitamin D supplements, regular exercise, medications to slow bone loss"
    },
    {
        "Code": 398,
        "name": "Rheumatoid Arthritis",
        "symptoms": "Joint pain, stiffness, swelling, fatigue, loss of appetite",
        "treatments": "Medications (nonsteroidal anti-inflammatory drugs, disease-modifying antirheumatic drugs), physical therapy, exercise"
    },
    {
        "Code": 399,
        "name": "Type 1 Diabetes",
        "symptoms": "Frequent urination, Increased thirst, Weight loss",
        "treatments": "Insulin therapy, Blood sugar monitoring, Healthy eating, Regular exercise"
    },
    {
        "Code": 400,
        "name": "Type 2 Diabetes",
        "symptoms": "Fatigue, Increased hunger, Slow healing of wounds",
        "treatments": "Oral medications, Insulin therapy (in some cases), Blood sugar monitoring, Exercise"
    },
]

client = QdrantClient(
    url=urlQdrant,
    api_key=apiQdrant
    )

client.create_collection(
    collection_name="Teste_Boock",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)

client.upload_points(
    collection_name="Teste_Boock",
    points=[
        models.PointStruct(
            id=idx, vector=encoder.encode(doc["symptoms"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)
