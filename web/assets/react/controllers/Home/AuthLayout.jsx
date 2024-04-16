import React from 'react';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Offcanvas from 'react-bootstrap/Offcanvas';
import { IoIosMenu } from "react-icons/io";
import Nav from 'react-bootstrap/Nav';
import axios from 'axios';

const AuthLayout = () => {
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    const handleLogout = () => {
        window.location.href = "/logout";
    }
    return (
        <>
            <Navbar className="bg-body-tertiary">
                <Container>

                    <IoIosMenu onClick={handleShow} style={{ height: '30px' }} />
                    <Offcanvas show={show} onHide={handleClose} style={{ width: '280px' }}>
                        <Offcanvas.Header closeButton>
                            <Offcanvas.Title>HireMatch</Offcanvas.Title>
                        </Offcanvas.Header>
                        <Offcanvas.Body>
                            <Nav defaultActiveKey="/home" className="flex-column">
                                <Nav.Link href="/home">HomePage</Nav.Link>
                                <Nav.Link eventKey="link-1">Profile</Nav.Link>
                                <Nav.Link eventKey="link-2">Offers</Nav.Link>
                                <Nav.Link onClick={handleLogout}>
                                    Log out
                                </Nav.Link>
                            </Nav>
                        </Offcanvas.Body>
                    </Offcanvas>
                </Container>
            </Navbar>
        </>
    );
}

export default AuthLayout;