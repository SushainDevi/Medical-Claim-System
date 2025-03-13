import { Route, Routes } from 'react-router-dom';
import { ProtectedRoute } from './routes';
import { ClaimsTable } from './components/ClaimsTable';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <ClaimsTable />
          </ProtectedRoute>
        }
      />
    </Routes>
  );
}