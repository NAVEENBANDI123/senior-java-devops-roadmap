# Part 3 — Best Learning Resources

> Curated, opinionated picks per topic. **Ratings are out of 10** and reflect quality + relevance for *this* roadmap (senior backend + DevOps). Pick **one** resource per topic and finish it — don't collect.

[← Roadmap](02-roadmap.md) · [Back to README](../README.md) · [Platforms →](04-platforms.md)

> ℹ️ Availability, pricing, and content change over time — verify current details on each provider's site before committing.

---

## 3.1 Core Java & JVM

| Topic | Best Free | Best Paid | Best YouTube | Best Docs | Difficulty | Rating |
|-------|-----------|-----------|--------------|-----------|:---:|:---:|
| Java Fundamentals | Java Brains, freeCodeCamp Java | Udemy: "Java Programming Masterclass" (Tim Buchalka) | Java Brains, Telusko | docs.oracle.com/javase | 🟢 | 9/10 |
| Streams & Functional | Baeldung Streams guides | Udemy: "Java Streams" focused courses | Java Brains, Devoxx talks | Oracle Stream API docs | 🟡 | 9/10 |
| Concurrency | Jenkov tutorials | Udemy/Educative concurrency courses | Defog Tech, Java Brains | Oracle Concurrency tutorial | 🔴 | 10/10 |
| JVM & GC | Baeldung JVM, Oracle GC tuning guide | Pluralsight JVM perf paths | "JVM internals" conf talks | OpenJDK / Oracle GC docs | 🔴 | 9/10 |
| Design Patterns | Refactoring.Guru | Udemy design patterns courses | Christopher Okhravi (patterns) | — | 🟡 | 10/10 |

**Mentor pick:** *Effective Java* (Joshua Bloch) — the single highest-leverage Java book. 10/10.

---

## 3.2 Databases & SQL

| Topic | Best Free | Best Paid | Best YouTube | Best Docs | Difficulty | Rating |
|-------|-----------|-----------|--------------|-----------|:---:|:---:|
| SQL | Mode SQL Tutorial, SQLBolt | Udemy "The Complete SQL Bootcamp" | freeCodeCamp SQL | — | 🟢 | 9/10 |
| PostgreSQL | PostgreSQL Tutorial (postgresqltutorial.com) | Udemy Postgres deep dives | Hussein Nasser (DB engineering) | postgresql.org/docs | 🟡 | 9/10 |
| Indexing & Optimization | use-the-index-luke.com | Educative DB performance | Hussein Nasser | DB-specific EXPLAIN docs | 🔴 | 10/10 |
| Transactions & Isolation | Vlad Mihalcea blog | "High-Performance Java Persistence" (Mihalcea) | Hussein Nasser | postgresql.org/docs MVCC | 🔴 | 10/10 |

---

## 3.3 Spring Ecosystem

| Topic | Best Free | Best Paid | Best YouTube | Best Docs | Difficulty | Rating |
|-------|-----------|-----------|--------------|-----------|:---:|:---:|
| Spring Boot | Spring Guides (spring.io/guides) | Spring Academy, Udemy (Chad Darby) | Amigoscode, Java Brains, Dan Vega | docs.spring.io | 🟡 | 10/10 |
| Spring Data JPA / Hibernate | Baeldung JPA series | Mihalcea's persistence course | Java Brains | Hibernate ORM docs | 🟡 | 9/10 |
| Spring Security / JWT / OAuth2 | Baeldung Security, Spring docs | Udemy Spring Security courses | Dan Vega, Amigoscode | docs.spring.io/spring-security | 🔴 | 9/10 |
| Testing (Testcontainers) | Testcontainers docs, Baeldung | — | — | testcontainers.org | 🟡 | 9/10 |
| Redis & Caching | Redis University (free) | — | Hussein Nasser | redis.io/docs | 🟡 | 9/10 |

**Mentor pick:** Official **Spring Guides** + **Baeldung** cover ~90% of daily needs for free. 10/10.

---

## 3.4 Microservices & Messaging

| Topic | Best Free | Best Paid | Best YouTube | Best Docs | Difficulty | Rating |
|-------|-----------|-----------|--------------|-----------|:---:|:---:|
| Microservices Patterns | microservices.io (Chris Richardson) | "Microservices Patterns" (book) | Amigoscode, Java Brains | spring.io/projects/spring-cloud | 🔴 | 10/10 |
| Kafka | Confluent Developer (free) | Udemy "Apache Kafka Series" (Stephane Maarek) | Confluent, Hussein Nasser | kafka.apache.org/documentation | 🔴 | 10/10 |
| Resilience4j | Resilience4j docs, Baeldung | — | — | resilience4j.readme.io | 🟡 | 8/10 |
| SAGA / CQRS / Outbox | microservices.io, Baeldung | — | — | — | 🔴 | 9/10 |

---

## 3.5 DevOps, Docker, Kubernetes

| Topic | Best Free | Best Paid | Best YouTube | Best Docs | Difficulty | Rating |
|-------|-----------|-----------|--------------|-----------|:---:|:---:|
| Linux / Shell | Linux Journey, OverTheWire (Bandit) | KodeKloud Linux | NetworkChuck | man pages, tldp.org | 🟢 | 9/10 |
| Git | Pro Git book (free) | — | The Net Ninja | git-scm.com/doc | 🟢 | 10/10 |
| Networking/HTTP | Cloudflare Learning Center, MDN HTTP | — | Hussein Nasser, Practical Networking | MDN, RFCs | 🟡 | 9/10 |
| Docker | Docker docs, "Docker for Beginners" | KodeKloud Docker, Udemy (Mumshad) | TechWorld with Nana | docs.docker.com | 🟡 | 10/10 |
| Kubernetes | kubernetes.io tutorials, Kelsey Hightower "Kubernetes the Hard Way" | KodeKloud CKA/CKAD | TechWorld with Nana | kubernetes.io/docs | 🔴 | 10/10 |
| Helm | Helm docs | KodeKloud Helm | — | helm.sh/docs | 🟡 | 8/10 |

**Mentor pick:** **TechWorld with Nana** (YouTube) + **KodeKloud** (hands-on labs) is the gold standard combo for DevOps. 10/10.

---

## 3.6 CI/CD

| Topic | Best Free | Best Paid | Best YouTube | Best Docs | Difficulty | Rating |
|-------|-----------|-----------|--------------|-----------|:---:|:---:|
| GitHub Actions | GitHub Actions docs | — | TechWorld with Nana | docs.github.com/actions | 🟡 | 9/10 |
| Jenkins | Jenkins handbook | KodeKloud Jenkins | TechWorld with Nana | jenkins.io/doc | 🟡 | 8/10 |
| SonarQube | SonarQube docs | — | — | docs.sonarqube.org | 🟡 | 8/10 |

---

## 3.7 Cloud (AWS) & IaC

| Topic | Best Free | Best Paid | Best YouTube | Best Docs | Difficulty | Rating |
|-------|-----------|-----------|--------------|-----------|:---:|:---:|
| AWS Fundamentals | AWS Skill Builder (free tier), freeCodeCamp | Udemy (Stephane Maarek SAA-C03), A Cloud Guru | freeCodeCamp, Be A Better Dev | docs.aws.amazon.com | 🔴 | 9/10 |
| AWS Cert (SAA) prep | AWS docs + free practice | Maarek + Tutorials Dojo practice exams | — | AWS Well-Architected | 🔴 | 10/10 |
| Terraform | HashiCorp Learn (free) | KodeKloud Terraform, Udemy | TechWorld with Nana | developer.hashicorp.com/terraform | 🔴 | 10/10 |

---

## 3.8 Observability

| Topic | Best Free | Best Paid | Best YouTube | Best Docs | Difficulty | Rating |
|-------|-----------|-----------|--------------|-----------|:---:|:---:|
| Prometheus & Grafana | Prometheus/Grafana docs, tutorials | KodeKloud Prometheus | TechWorld with Nana | prometheus.io, grafana.com/docs | 🔴 | 9/10 |
| ELK / Loki | Elastic free training, Grafana Loki docs | — | — | elastic.co/guide | 🟡 | 8/10 |
| OpenTelemetry | OTel docs | — | Honeycomb/OTel talks | opentelemetry.io/docs | 🔴 | 8/10 |

---

## 3.9 System Design

| Topic | Best Free | Best Paid | Best YouTube | Best Docs | Difficulty | Rating |
|-------|-----------|-----------|--------------|-----------|:---:|:---:|
| System Design | "System Design Primer" (GitHub) | Educative "Grokking Modern System Design", ByteByteGo | ByteByteGo, Gaurav Sen, Hussein Nasser | — | 🔴 | 10/10 |
| DDIA concepts | — | "Designing Data-Intensive Applications" (Kleppmann) | — | — | 🔴 | 10/10 |

**Mentor pick:** *Designing Data-Intensive Applications* is the most important book for senior backend engineers. Read it slowly. 10/10.

---

## 📚 Essential Book Shelf (highest leverage)

| Book | Domain | Priority |
|------|--------|:---:|
| Effective Java — Bloch | Core Java | ⭐⭐⭐ |
| Java Concurrency in Practice — Goetz | Concurrency | ⭐⭐⭐ |
| Designing Data-Intensive Applications — Kleppmann | Distributed/System Design | ⭐⭐⭐ |
| High-Performance Java Persistence — Mihalcea | JPA/DB | ⭐⭐ |
| Clean Code / A Philosophy of Software Design | Design | ⭐⭐ |
| The Phoenix Project / The DevOps Handbook | DevOps culture | ⭐⭐ |
| Microservices Patterns — Richardson | Microservices | ⭐⭐ |

[← Roadmap](02-roadmap.md) · [Back to README](../README.md) · [Platforms →](04-platforms.md)
