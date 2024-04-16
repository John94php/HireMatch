import React from 'react';
import { BrowserRouter as Router, Route, Routes  } from 'react-router-dom';
import Menu from './Navbar';
import Hello from './Hello'
import AboutPage from './AboutPage'
import SigninPage from './Auth/SigninPage'
import SignupPage from './Auth/SignupPage'
const AppRouter = () => {
  return (
    <Router>
      <Menu />
      <Routes>
        <Route exact path="/" element={<Hello/>} />
        <Route path="/about" element={<AboutPage/>} />
        <Route path="/login" element={<SigninPage/>} />
        <Route path="/register" element={<SignupPage/>} />
      </Routes>
    </Router>
  );
}

export default AppRouter;