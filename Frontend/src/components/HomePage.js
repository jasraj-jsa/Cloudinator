import React, { useState } from "react";
import {
  Form,
  FormGroup,
  Label,
  Input,
  Button,
  Card,
  CardText,
  CardBody,
  CardTitle,
  CardSubtitle,
  Spinner,
} from "reactstrap";
const HomePage = (props) => {
  const DeallocateResource = (resourceId, resourceGroup, owner) => {
    setIsRefreshed(false);
    fetch("/deallocateResource", {
      method: "POST",
      body: JSON.stringify({
        resourceId,
        owner,
        resourceGroup,
      }),
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    })
      .then((res) => {
        if (res.status == 200) return res.json();
        return {};
      })
      .then((data) => {
        // console.log(data);
        setIsRefreshed(true);
        alert("Resource Deallocated Successfully!");
      })
      .catch((err) => console.log(err));
  };
  const NotifyUser = (resource) => {
    const recentUser1 =
      !resource["recentUser1"] || resource["recentUser1"] === ""
        ? ""
        : resource["recentUser1"];
    const recentUser2 =
      !resource["recentUser2"] || resource["recentUser2"] === ""
        ? ""
        : resource["recentUser2"];
    const resourceStatus =
      !resource["resourceStatus"] || resource["resourceStatus"] === ""
        ? ""
        : resource["resourceStatus"];
    const oldResourceGroup =
      !resource["oldResourceGroup"] || resource["oldResourceGroup"] === ""
        ? ""
        : resource["oldResourceGroup"];
    const owner = resource["owner"];
    const resourceName = resource["resourceName"];
    const resourceType = resource["resourceType"];
    const resourceGroup = resource["resourceGroup"];
    const subscriptionName =
      !resource["subscriptionName"] || resource["subscriptionName"] === ""
        ? ""
        : resource["subscriptionName"];
    const request_body = JSON.stringify({
      recentUser1,
      recentUser2,
      oldResourceGroup,
      owner,
      resourceName,
      resourceType,
      subscriptionName,
      resourceStatus,
      resourceGroup,
      oldResourceGroup,
    });

    setIsRefreshed(false);
    fetch("/notifyUser", {
      method: "POST",
      body: request_body,
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    })
      .then((res) => {
        if (res.status == 200) return res.json();
        return {};
      })
      .then((data) => {
        // console.log(data);
        setIsRefreshed(true);
        alert("User(s) notified successfully!");
      })
      .catch((err) => console.log(err));
  };
  const onRefresh = (event) => {
    if (!searchQuery) {
      alert("Please enter an input to refresh the data for");
      return;
    }
    setIsRefreshed(false);
    event.preventDefault();
    fetch("/refreshDB?username=" + searchQuery, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    })
      .then((res) => {
        if (res.status == 200) return res.json();
        return {};
      })
      .then((data) => {
        alert("Data Refresh Successful!!");
        setIsRefreshed(true);
      })
      .catch((err) => console.log(err));
  };
  const onSearch = (event) => {
    event.preventDefault();
    fetch("/searchDB?username=" + searchQuery, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    })
      .then((res) => {
        if (res.status == 200) return res.json();
        return {};
      })
      .then((data) => {
        // console.log(data);
        if (data.length == 0) {
          setOnSearchClick(false);
        } else setResources(data);
      })
      .catch((err) => console.log(err));
  };
  const [searchQuery, setSearchQuery] = useState("");
  const [resources, setResources] = useState([]);
  const [onSearchClick, setOnSearchClick] = useState(false);
  const [isRefreshed, setIsRefreshed] = useState(true);
  const RenderSearch = ({ resource }) => {
    return (
      <CardBody>
        <CardTitle>
          <b>{resource["resourceName"]}</b>
          <Button
            style={{ float: "right", marginLeft: 10 }}
            color="info"
            outline
            disabled={!isRefreshed}
            onClick={() => {
              NotifyUser(resource);
            }}
          >
            <span className="fa fa-bell fa-lg"></span>
          </Button>
          <Button
            style={{ float: "right" }}
            color="danger"
            outline
            disabled={
              !isRefreshed ||
              (resource["resourceStatus"] &&
                resource["resourceStatus"] != "Active")
            }
            onClick={() => {
              DeallocateResource(
                resource["resourceId"],
                resource["resourceGroup"],
                resource["owner"]
              );
            }}
          >
            <span className="fa fa-stop fa-lg"></span>
          </Button>
        </CardTitle>
        <CardSubtitle>
          <b>Owner:</b> {resource["owner"]}{" "}
        </CardSubtitle>
        <br />
        <CardText>
          <b>Resource Id:</b> {resource["resourceId"]}
        </CardText>
        <CardText>
          <b>Resource Group:</b> {resource["resourceGroup"]}
        </CardText>
        <CardText>
          <b>Resource Type:</b> {resource["resourceType"]}
        </CardText>
        <CardText>
          <b>Resource Status:</b> {resource["resourceStatus"]}
        </CardText>
        <CardText>
          <b>Resource Location:</b> {resource["resourceLocation"]}
        </CardText>
        {!resource["resourceKind"] || resource["resourceKind"] === "" ? (
          <></>
        ) : (
          <>
            <CardText>
              <b>Resource Kind:</b> {resource["resourceKind"]}
            </CardText>
          </>
        )}
        {!resource["oldResourceGroup"] ||
        resource["oldResourceGroup"] === "" ? (
          <></>
        ) : (
          <>
            <CardText>
              <b>Original Resource Group:</b> {resource["oldResourceGroup"]}
            </CardText>
          </>
        )}
        {!resource["recentUser1"] || resource["recentUser1"] === "" ? (
          <></>
        ) : (
          <>
            <CardText>
              <b>Recent User 1:</b> {resource["recentUser1"]}
            </CardText>
          </>
        )}
        {!resource["recentUser2"] || resource["recentUser2"] === "" ? (
          <></>
        ) : (
          <>
            <CardText>
              <b>Recent User 2:</b> {resource["recentUser2"]}
            </CardText>
          </>
        )}
        {!resource["UsageCostUSD"] || resource["UsageCostUSD"] === "" ? (
          <></>
        ) : (
          <>
            <CardText>
              <b>Usage Cost [This Month] (in USD):</b>{" "}
              {resource["UsageCostUSD"]}
            </CardText>
          </>
        )}
        {!resource["CPU-Utilization"] || resource["CPU-Utilization"] === "" ? (
          <></>
        ) : (
          <>
            <CardText>
              <b>CPU Utilization [This Month]:</b> {resource["CPU-Utilization"]}
            </CardText>
          </>
        )}
      </CardBody>
    );
  };
  return (
    <div
      style={{
        display: "flex",
        minHeight: 500,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div>
        <Button
          value="refresh"
          color="success"
          style={{ marginTop: 25, float: "right", marginRight: 50 }}
          disabled={!isRefreshed}
          outline
          onClick={onRefresh}
        >
          <span className="fa fa-lg fa-refresh"></span>
        </Button>
        <Form onSubmit={onSearch}>
          <FormGroup>
            <br />
            <Label>
              <h2>
                <b>Cloudinator </b>
                <i>Search</i>
              </h2>
            </Label>
          </FormGroup>
          <br />
          <FormGroup>
            <Label>
              <Input
                type="search"
                id="search"
                name="query"
                placeholder="Enter an email adress..."
                size="100"
                onChange={(evt) => {
                  setSearchQuery(evt.target.value);
                }}
                value={searchQuery}
                required
              />
            </Label>
          </FormGroup>
          <br />
          <Button
            type="submit"
            value="search"
            color="primary"
            onClick={() => {
              if (searchQuery) setOnSearchClick(true);
            }}
            disabled={!isRefreshed}
          >
            Search
          </Button>

          <div id="information"></div>
        </Form>
        {onSearchClick ? (
          <div>
            {resources.length == 0 ? (
              <Spinner style={{ marginTop: 20 }}></Spinner>
            ) : (
              <>
                {resources.map((res) => (
                  <div>
                    <Card style={{ margin: 50 }}>
                      <RenderSearch resource={res} />
                    </Card>
                  </div>
                ))}
              </>
            )}
          </div>
        ) : (
          <></>
        )}
      </div>
    </div>
  );
};

export default HomePage;
