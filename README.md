# Hotel RAG Assistant

## 🎯 Goal
Build a production-ready **Hotel Search Assistant** that uses **Retrieval-Augmented Generation (RAG)** to answer user queries about hotels (amenities, cancellation policy, reviews, etc.) with high accuracy, low latency, and cost efficiency.

This project demonstrates how to combine **LLMs, vector databases, and Kubernetes** into a reliable AI-powered search system — with observability, security, and scalability built-in.

---

## 🏗️ Architecture (MVP → Production)
1. **Data Layer**
   - Store hotel descriptions, policies, and reviews.
   - Generate embeddings and index into **pgvector** (Postgres) or **Qdrant**.

2. **Retrieval Layer**
   - Retrieve relevant passages using semantic search.
   - Evaluate results (recall@k, hallucination rate).

3. **LLM Layer**
   - Use an LLM (OpenAI, Anthropic, or local) to generate answers.
   - Wrap orchestration using **LangChain**.

4. **API Layer**
   - Expose REST/GraphQL endpoints (Node.js or FastAPI).
   - `/ask?query=...` → returns hotel-specific answer with sources.

5. **Infra Layer**
   - Containerize with Docker.
   - Deploy on Kubernetes with monitoring, logging, and scaling.
   - CI/CD pipeline for safe rollouts.

6. **Security Layer**
   - Input validation, prompt logging with masking.
   - Role-based access for APIs.

---

## 📊 Success Metrics
- Response latency < 2s (p95).
- Reduce irrelevant answers by 40% compared to baseline search.
- < 5% hallucination rate (evaluated on test queries).
- Cost per query tracked and optimized.

---

## 🚀 Roadmap
### Month 1–3 (MVP)
- [ ] Ingest hotel dataset and generate embeddings.
- [ ] Set up pgvector or Qdrant for retrieval.
- [ ] Build LangChain pipeline for RAG.
- [ ] Create `/ask` API endpoint.

### Month 4–6 (Production-ready)
- [ ] Add CI/CD pipeline.
- [ ] Deploy on Kubernetes (minikube → cloud).
- [ ] Implement observability (logging, metrics, dashboards).
- [ ] Add security features.

### Month 7–12 (Scaling & Visibility)
- [ ] Write a blog post about the architecture.
- [ ] Demo at a meetup or internal company session.
- [ ] Mentor juniors or expand to car search assistant.

---

## 🗂️ Folder Structure
