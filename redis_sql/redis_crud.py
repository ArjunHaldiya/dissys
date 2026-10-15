import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def create(id, name, email):
    r.hset(f"user:{id}", mapping={"name":name, "email":email})

def read(id):
    return r.hgetall(f"user:{id}")

def update(id, new_email):
    r.hset(f"user:{id}", "email", new_email)

def delete(id):
    r.delete(f"user:{id}")


if __name__ == "__main__":
    create(1, "Arjun Haldiya", "arjunhaldiya@gmail.com")
    print(read(1))
    update(99, "arjunhaldiya91@gmail.com")
    print(read(99))
    delete(1)
    print(read(1))