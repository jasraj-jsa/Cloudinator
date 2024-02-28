import React, { useState } from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';
// import { withRouter } from 'react-router';
import Header from "./Header";
import Footer from "./Footer";
import HomePage from './HomePage';
import Contact from "./Contact";
const Main = (props) => {
        return (
            <div style={{backgroundColor: "#BCEBFD"}}>
                <Header />
                <Switch>
                    <Route path='/home' component={HomePage} />
                    <Route path='/contact' component={Contact} />
                    <Redirect to="/home" />
                </Switch>
                <Footer />
            </div>
        );
    
}

export default Main;