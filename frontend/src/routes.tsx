import { Auth } from 'aws-amplify';
import { Navigate } from 'react-router-dom';

export const ProtectedRoute = ({ children }) => {
  const isAuthenticated = async () => {
    try {
      await Auth.currentAuthenticatedUser();
      return true;
    } catch {
      return false;
    }
  };
  return isAuthenticated ? children : <Navigate to="/" />;
};