import React, { useState } from 'react';
import {
    Navbar, NavbarBrand, Nav, NavbarToggler, Collapse, NavItem, Jumbotron,
    Button, Modal, ModalHeader, ModalBody,
    Form, FormGroup, Input, Label,NavLink
} from 'reactstrap';
// import { NavLink } from 'react-router-dom';
const Header = (props) => {
        return (
            <div>
                <Navbar dark expand="md">
                    <div className="container">
                        <NavbarBrand className="mr-auto" href="/"><img src='assets/images/logo.png' height="35" width="35" alt='Cloudinator' /></NavbarBrand>
                        <Collapse navbar>
                            <Nav navbar>
                                <NavItem>
                                    <NavLink className="nav-link" href='/home'><span className="fa fa-home fa-lg"></span> Home</NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink className="nav-link" href='/contact'><span className="fa fa-address-card fa-lg"></span> Contact Us</NavLink>
                                </NavItem>
                            </Nav>
                            <Nav style={{marginLeft: 820}} navbar>
                                <NavItem>
                                    <NavLink href='https://app.powerbi.com/groups/ea928f81-6fc6-4e3a-9c47-f1903e4b12f2/reports/4596a49d-859c-4ac4-8c5d-8d76be0953bc/ReportSection' target="_blank"><Button outline color="info"><span className="fa fa-windows fa-lg"></span> Power Bi Dasboard</Button></NavLink>
                                </NavItem>
                            </Nav>
                        </Collapse>
                    </div>
                </Navbar>
                <Jumbotron>
                    <div className="container">
                        <div className="row row-header">
                            <div className="col-12 col-sm-6">
                                <h1>Cloudinator</h1>
                                <p> A platform to manage your cloud resources. Get a complete picture of the activtiy, usage and cost of the resources and decide which one's need deallocatiing.  </p>
                            </div>
                        </div>
                    </div>
                </Jumbotron>
            </div>
        );
    
}

export default Header;