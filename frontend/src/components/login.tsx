import { Auth } from 'aws-amplify';
import { useNavigate } from 'react-router-dom';

export const Login = () => {
  const navigate = useNavigate();
  const handleLogin = async () => {
    try {
      await Auth.signIn("username", "password");
      navigate("/dashboard");
    } catch (error) {
      console.error("Login failed:", error);
    }
  };
  return <button onClick={handleLogin}>Login</button>;
};