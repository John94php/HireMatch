import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Alert from 'react-bootstrap/Alert';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import axios from 'axios';
import { createBrowserHistory } from 'history';
import { Navigate } from 'react-router-dom';

const SigninPage = () => {
  const history = createBrowserHistory();

  const [showAlert, setShowAlert] = useState(true);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = () => {
    setIsLoading(true); // Włącz ekran ładowania

    const loginUrl = "/api_login";
    const data = {
      username: username,
      password: password
    };
    axios.post(loginUrl, data)
      .then(response => {
        setLoggedIn(true); 
      })
      .catch(error => {
        console.error('Error:', error);
        setIsLoading(false); 

      });
  }
  if (loggedIn) {
    window.location.href = "/home"
  }
  return (
    <>
      {loggedIn } 
      {showAlert && (
        <Alert key="primary" variant="primary">
          Log in to your account
        </Alert>
      )}
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="formHorizontalEmail">
          <Form.Label column sm={2}>
            Email
          </Form.Label>
          <Col sm={10}>
            <Form.Control type="email" placeholder="john@doe.com" value={username} onChange={(e) => setUsername(e.target.value)} />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="formHorizontalPassword">
          <Form.Label column sm={2}>
            Password
          </Form.Label>
          <Col sm={10}>
            <Form.Control type="password" placeholder="Your password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </Col>
        </Form.Group>
        <Form.Group as={Row} className="mb-3" controlId="formHorizontalCheck">
          <Col sm={{ span: 10, offset: 2 }}>
            <Form.Check label="Remember me" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3">
          <Col sm={{ span: 10, offset: 2 }}>
            {/* Przycisk logowania będzie nieaktywny w trakcie ładowania */}
            <Button type="submit" onClick={handleLogin} disabled={isLoading}>
              {isLoading ? 'Loading...' : 'Sign in'}
            </Button>
          </Col>
        </Form.Group>
      </Form>


    </>
  );
}

export default SigninPage;
