import asyncio
import aiosqlite

# Database file path
DATABASE_PATH = 'your_database.db'

# Asynchronous function to fetch all users
async def async_fetch_users():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            return users

# Asynchronous function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            older_users = await cursor.fetchall()
            return older_users

# Function to run both queries concurrently
async def fetch_concurrently():
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return all_users, older_users

# Running the concurrent fetch
if __name__ == "__main__":
    all_users, older_users = asyncio.run(fetch_concurrently())
    print("All Users:", all_users)
    print("Users Older Than 40:", older_users)
