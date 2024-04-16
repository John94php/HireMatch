import React from 'react';
import { BrowserRouter as Router, Route, Routes  } from 'react-router-dom';
import Main from './Main'
import AuthLayout from './AuthLayout';
const AuthApp = () => {
  return (
    <>
    <AuthLayout />
    <Router>
      <Routes>
        <Route exact path="/home" element={<Main/>} />
      </Routes>
    </Router>

    </>
      );
}

export default AuthApp;