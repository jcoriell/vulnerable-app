HOME = """
<!DOCTYPE html>
<html>
<head><title>Home</title><style>
  body { font-family: Arial, sans-serif; max-width: 600px; margin: 80px auto; text-align: center; }
  a { display: inline-block; margin: 10px; padding: 10px 24px; background: #4a90e2; color: white;
      text-decoration: none; border-radius: 4px; }
  a:hover { background: #357abd; }
</style></head>
<body>
  <h1>Welcome</h1>
  <p>A simple (vulnerable) web application.</p>
  <a href="/login">Login</a>
  <a href="/register">Create Account</a>
</body>
</html>
"""

LOGIN = """
<!DOCTYPE html>
<html>
<head><title>Login</title><style>
  body { font-family: Arial, sans-serif; max-width: 400px; margin: 80px auto; }
  input { display: block; width: 100%; padding: 8px; margin: 8px 0; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
  button { width: 100%; padding: 10px; background: #4a90e2; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
  button:hover { background: #357abd; }
  .error { color: red; margin-bottom: 10px; }
  a { color: #4a90e2; }
</style></head>
<body>
  <h2>Login</h2>
  {% if error %}<p class="error">{{ error }}</p>{% endif %}
  <form method="POST">
    <label>Username</label>
    <input type="text" name="username" placeholder="Enter username">
    <label>Password</label>
    <input type="password" name="password" placeholder="Enter password">
    <button type="submit">Login</button>
  </form>
  <p><a href="/">← Back to home</a> &nbsp;|&nbsp; <a href="/register">Create an account</a></p>
</body>
</html>
"""

REGISTER = """
<!DOCTYPE html>
<html>
<head><title>Create Account</title><style>
  body { font-family: Arial, sans-serif; max-width: 400px; margin: 80px auto; }
  input { display: block; width: 100%; padding: 8px; margin: 8px 0; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
  button { width: 100%; padding: 10px; background: #5cb85c; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
  button:hover { background: #4cae4c; }
  .error { color: red; margin-bottom: 10px; }
  .success { color: green; margin-bottom: 10px; }
  a { color: #4a90e2; }
</style></head>
<body>
  <h2>Create Account</h2>
  {% if error %}<p class="error">{{ error }}</p>{% endif %}
  {% if success %}<p class="success">{{ success }}</p>{% endif %}
  <form method="POST">
    <label>Username</label>
    <input type="text" name="username" placeholder="Choose a username">
    <label>Password</label>
    <input type="password" name="password" placeholder="Choose a password">
    <button type="submit">Create Account</button>
  </form>
  <p><a href="/">← Back to home</a> &nbsp;|&nbsp; <a href="/login">Already have an account?</a></p>
</body>
</html>
"""

DASHBOARD = """
<!DOCTYPE html>
<html>
<head><title>Dashboard</title><style>
  body { font-family: Arial, sans-serif; max-width: 700px; margin: 60px auto; }
  .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #ddd; padding-bottom: 16px; margin-bottom: 24px; }
  .card { background: #f5f7fa; border-radius: 8px; padding: 20px; margin-bottom: 16px; }
  .logout { padding: 8px 16px; background: #e74c3c; color: white; text-decoration: none; border-radius: 4px; }
  .logout:hover { background: #c0392b; }
  h1 { margin: 0; font-size: 24px; }
</style></head>
<body>
  <div class="header">
    <h1>Dashboard</h1>
    <a href="/logout" class="logout">Logout</a>
  </div>
  <div class="card">
    <h3>👋 Hello, {{ username }}!</h3>
    <p>You are logged in. Welcome to your dashboard.</p>
  </div>
  <div class="card">
    <h3>Your Profile</h3>
    <p><strong>Username:</strong> {{ username }}</p>
    <p><strong>User ID:</strong> {{ user_id }}</p>
  </div>
</body>
</html>
"""
