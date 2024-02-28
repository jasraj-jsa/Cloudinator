import React from 'react';
const Contact = () => {
    return (
        <div style={{display:"flex", minHeight: 500,justifyContent: "center", alignItems:"center"}}>
                <div className="row row-content" style={{borderWidth: 0}}>
                    <div className="col-12">
                        <h3>Location Information</h3>
                    </div>
                    <div className="col-12 col-sm-10 offset-sm-1">
                        <h5>Our Address</h5>
                        <address>
                            Prestige Dynasty, Phase, 33/2, Ulsoor Rd, Sivanchetti Gardens <br/>
                            Bengaluru, Karnataka 560042 <br/>
                            <i className="fa fa-phone"></i>: +852 1234 5678<br />
                            <i className="fa fa-fax"></i>: +852 8765 4321<br />
                            <i className="fa fa-envelope"></i>: <a href="mailto:cloudinator@citrix.com">cloudinator@citrix.com</a>
                        </address>
                    </div>
                    <div className="col-12 col-sm-10 offset-sm-1">
                        <div className="btn-group" role="group">
                            <a role="button" className="btn btn-primary" href="tel:+85212345678"><i className="fa fa-phone"></i> Call</a>
                            <a role="button" className="btn btn-info"><i className="fa fa-skype"></i> Skype</a>
                            <a role="button" className="btn btn-success" href="mailto:cloudinator@citrix.com"><i className="fa fa-envelope-o"></i> Email</a>
                        </div>
                    </div>
                </div>
            </div>
    );
}

export default Contact;