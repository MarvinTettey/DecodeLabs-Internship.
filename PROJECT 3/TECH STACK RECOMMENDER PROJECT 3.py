# Decode Labs - Artificial Intelligence Project 3
# AI Recommendation Logic — Tech Stack Recommender
# Algorithm: TF-IDF Vectorization + Cosine Similarity
# Developed by: Marvin Tettey

# ---------------------------------------------------
# STEP 1: IMPORT LIBRARIES
# ---------------------------------------------------
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("=" * 60)
print("🧭 DecodeLabs AI Project 3: Tech Stack Recommender 🧭")
print("Mapping your skills to the best-fit career path")
print("=" * 60)

# ---------------------------------------------------
# STEP 2: INGESTION - LOAD THE DATASET
# ---------------------------------------------------
# raw_skills.csv contains job roles ("items") and their associated
# skills. This acts as our knowledge base of careers to recommend from.

df = pd.read_csv('raw_skills.csv')

print(f"\n📂 Loaded {len(df)} job roles from raw_skills.csv")

# Replace commas with spaces so TF-IDF treats each skill as a separate
# "word" in the same vocabulary space (e.g. "Machine Learning" stays
# as two words to align with how a user might type it)
df['skills_text'] = df['skills'].str.replace(',', ' ')

# ---------------------------------------------------
# STEP 3: INGESTION - CAPTURE USER INPUT
# ---------------------------------------------------
# Per the spec: the script must accept a minimum of 3 user inputs
# to ensure sufficient data density for accurate matching.

def get_user_skills():
    """Prompts the user for their skills/interests (minimum 3)."""
    print("\n💡 Enter at least 3 skills or interests you have.")
    print("Example: Python, Cloud Computing, Automation")
    raw = input("Your skills (comma-separated): ")
    skills = [s.strip() for s in raw.split(',') if s.strip() != '']

    while len(skills) < 3:
        print(f"⚠️  You entered {len(skills)} skill(s). Please enter at least 3.")
        raw = input("Your skills (comma-separated): ")
        skills = [s.strip() for s in raw.split(',') if s.strip() != '']

    return skills

user_skills = get_user_skills()
user_profile_text = ' '.join(user_skills)

print(f"\n✅ Profile captured: {user_skills}")

# ---------------------------------------------------
# STEP 4: PROCESS - VECTOR MAPPING (TF-IDF)
# ---------------------------------------------------
# Machines understand numbers, not words. TF-IDF converts both the
# job descriptions and the user's profile into numerical vectors
# within the SAME shared vocabulary space, so they can be compared.
#
# We combine the user profile with the job dataset before fitting
# the vectorizer, ensuring both sets of vectors share identical
# dimensions/vocabulary.

corpus = list(df['skills_text']) + [user_profile_text]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# The last row of the matrix is the user's vector; everything before
# it belongs to the job roles
job_vectors = tfidf_matrix[:-1]
user_vector = tfidf_matrix[-1]

print("\n⚙️  Skills converted to TF-IDF vectors")
print(f"Vocabulary size: {len(vectorizer.get_feature_names_out())} unique terms")

# ---------------------------------------------------
# STEP 5: SCORING - COSINE SIMILARITY
# ---------------------------------------------------
# Cosine similarity measures the angle between two vectors, making
# it ideal here since job descriptions vary in length but we only
# care about the ORIENTATION (overlap of skills), not the size.

similarity_scores = cosine_similarity(user_vector, job_vectors).flatten()

df['similarity_score'] = similarity_scores

print("\n📐 Cosine similarity calculated against all job roles")

# ---------------------------------------------------
# STEP 6: SORTING - RANK BY RELEVANCE
# ---------------------------------------------------
# Sort the scored dataset in descending order so the most relevant
# job roles rise to the top.

ranked_jobs = df.sort_values(by='similarity_score', ascending=False)

# ---------------------------------------------------
# STEP 7: FILTERING - TOP-N RECOMMENDATIONS
# ---------------------------------------------------
# Truncate the list to prevent choice overload. We display only the
# Top 3 highest-scoring matches.

TOP_N = 3
top_matches = ranked_jobs.head(TOP_N)

# ---------------------------------------------------
# STEP 8: OUTPUT - DISPLAY RECOMMENDATIONS
# ---------------------------------------------------
print("\n" + "=" * 60)
print(f"🎯 TOP {TOP_N} RECOMMENDED CAREER PATHS FOR YOU")
print("=" * 60)

if top_matches['similarity_score'].max() == 0:
    print("\n⚠️  No strong matches found. Try entering more common")
    print("tech skills (e.g. Python, SQL, AWS, JavaScript).")
else:
    for rank, (_, row) in enumerate(top_matches.iterrows(), start=1):
        match_percent = row['similarity_score'] * 100
        print(f"\n#{rank}  {row['job_role']}")
        print(f"     Match Score : {match_percent:.1f}%")
        print(f"     Key Skills  : {row['skills']}")

print("\n✅ Project 3 completed successfully!")
