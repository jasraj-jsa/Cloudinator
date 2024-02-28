import React, {useState} from 'react';

const Footer = (props) => {
    return (
        <div className="footer">
            <div className="container">
                <div className="row justify-content-center">
                    <div className="col-4 offset-1 col-sm-2">
                        <h5>Links</h5>
                        <ul className="list-unstyled">
                            <li><a href="/home">Home</a></li>
                            <li><a href="/contact">Contact</a></li>
                        </ul>
                    </div>
                    <div className="col-7 col-sm-5">
                        <h5>Our Address</h5>
                        <address>
                        Prestige Dynasty, Phase, 33/2, Ulsoor Rd, Sivanchetti Gardens<br/>
                        Bengaluru, Karnataka 560042<br />
                            <i className="fa fa-phone fa-lg"></i>: +852 1234 5678<br />
                            <i className="fa fa-fax fa-lg"></i>: +852 8765 4321<br />
                            <i className="fa fa-envelope fa-lg"></i>: <a href="mailto:cloudinator@citrix.com">
                                cloudinator@citrix.com</a>
                        </address>
                    </div>
                    <div className="col-12 col-sm-4 align-self-center">
                        <div className="text-center">
                            <a className="btn btn-social-icon btn-facebook" href="https://www.facebook.com/Citrix/"><i className="fa fa-facebook"></i></a>
                            <a className="btn btn-social-icon btn-linkedin" href="https://www.linkedin.com/company/citrix"><i className="fa fa-linkedin"></i></a>
                            <a className="btn btn-social-icon btn-twitter" href="https://twitter.com/citrix?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"><i className="fa fa-twitter"></i></a>
                            <a className="btn btn-social-icon btn-google" href="https://www.youtube.com/citrix"><i className="fa fa-youtube"></i></a>
                            <a className="btn btn-social-icon" href="mailto:"><i className="fa fa-envelope-o"></i></a>
                        </div>
                    </div>
                </div>
                <div className="row justify-content-center">
                    <div className="col-auto">
                        <br /><p>© Copyright 2021 Cloudinator</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Footer;