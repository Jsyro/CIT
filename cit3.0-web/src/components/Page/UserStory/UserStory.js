import { useState, useEffect } from "react";
import { Container, Button, Row, Col } from "react-bootstrap";
import { ArrowRight } from "react-bootstrap-icons";
import axios from "axios";
import { useHistory } from "react-router-dom";
import ReactHtmlParser from "react-html-parser";

import "../HomePage/HomePage.scss";

import { useDispatch, useSelector } from "react-redux";
import { getOptions, setOptions } from "../../../store/actions/options";
import { userStoryPaths } from "../../../data/userStoryPaths.json";
import { useKeycloakWrapper } from "../../../hooks/useKeycloakWrapper";
import "./UserStory.css";
import UserStoryItem from "../../UserStoryItem/UserStoryItem";
import ReportOverview from "../../ReportOverview/ReportOverview";
import ReportCompare from "../../ReportCompare/ReportCompare";
import ReportCriteriaSearch from "../../ReportCriteriaSearch/ReportCriteriaSearch";

export default function UserStoryV2() {
  let loading = false;
  const [userOptions, setAllOptions] = useState([]);
  const [showUserStoryText, setShowUserStoryText] = useState(true);
  const [showReport, setShowReport] = useState(false);
  const [who, setWho] = useState("");
  const [isGoButton, setIsGoButton] = useState(false);
  const [isOkButton, setIsOkButton] = useState(false);
  const [redirectUrl, setRedirectUrl] = useState("");
  const [areaType, setAreaType] = useState("");
  const [areaFilterId, setAreaFilterId] = useState("");
  const [areaSearchFilter, setAreaSearchFilter] = useState("");
  const [powerBiReport, setPowerBiReport] = useState(null);
  const [communities, setCommunities] = useState(null);
  const [regionals, setRegionals] = useState(null);

  const keycloak = useKeycloakWrapper();

  const history = useHistory();
  const dispatch = useDispatch();

  const userName = keycloak ? keycloak.firstName : "";

  const showResult = (urlPath) => {
    if (!urlPath) return;

    if (urlPath && urlPath.includes("powerbi")) {
      setPowerBiReport(urlPath);
      setShowUserStoryText(false);
      setShowReport(true);
      return;
    }
    history.push(urlPath);
  };

  const regionalDistricts = useSelector(
    (state) => state.options.regionalDistricts
  );

  const statuses = useSelector((state) => state.options.statuses);
  if (!loading && (!statuses.length || !regionalDistricts.length)) {
    loading = true;
    getOptions().then((response) => {
      dispatch(setOptions(response.data));
      loading = false;
    });
  }

  useEffect(() => {
    axios.get("/api/opportunity/options").then((data) => {
      const commNames = data.data.communities.map((x) => ({
        value: x.id,
        label: x.place_name,
      }));

      setCommunities(commNames);

      const regNames = data.data.regionalDistricts.map((x) => ({
        value: x.id,
        label: x.name,
      }));

      setRegionals(regNames);
    });
  }, []);

  useEffect(() => {
    const option = userStoryPaths.find((x) => x.code === "START");
    option.preTextLabel = option.preText;
    setAllOptions([option]);
  }, []);

  const resetUserStory = () => {
    const options = userStoryPaths.find((x) => x.code === "START");
    setAllOptions([options]);
    setIsOkButton(false);
    setIsGoButton(false);
  };

  const handleUserStoryChange = (e) => {
    let param;

    if (e.length === 0) {
      setIsOkButton(false);
      setIsGoButton(false);
      return;
    }

    if (Array.isArray(e)) {
      param = e.find((x, index) => index < 1);
    } else {
      param = e;
    }

    if (param && !param.code) {
      const zone = userStoryPaths.find((x) => x.group === "zone-type-list");
      if (zone) {
        param.code = zone.code;
        param.group = zone.group;
        param.url = zone.url;
      }
      setAreaSearchFilter(param.label);
    }

    if (param && param.group === "who") {
      setWho(param);
    }

    const groupIndex = userOptions.findIndex((x) => x.group === param.group);

    let newUserOptions = [];
    if (groupIndex > 0) {
      newUserOptions = userOptions.filter((x, index) => index < groupIndex);
    } else {
      newUserOptions = userOptions;
    }

    const userOption = userStoryPaths.find((x) => x.code === param.code);

    if (param.group === "zone") {
      setAreaType(userOption.label);
      setAreaFilterId(userOption.code.toLowerCase());
    }

    if (userOption.code.includes("REGIONALDISTRICTS")) {
      userOption.user_story_paths = regionals;
    }

    if (userOption.code.includes("COMMUNITYAREA")) {
      userOption.user_story_paths = communities;
    }

    let replaceText = userOption.preText;
    replaceText = replaceText.replace(
      "{ZONE-TYPE-1}",
      userOption.label.slice(0, -1)
    );
    replaceText = replaceText.replace("{ZONE-TYPE-2}", areaType);
    replaceText = replaceText.replace("{ZONE-SEARCH-FILTER}", param.label);
    userOption.preTextLabel = replaceText;

    setAllOptions([...newUserOptions, userOption]);

    if (param.code.includes("-YES")) {
      setIsOkButton(false);
      showResult(param.url);
      return;
    }

    const isLastOption = userOption.user_story_paths.length < 2;

    if (userOption.code.includes("-GO") || isLastOption) {
      setIsGoButton(true);
      setIsOkButton(false);
      setRedirectUrl(param.url);
    } else {
      setIsGoButton(false);
      setIsOkButton(false);
    }

    if (userOption.code.includes("-NO")) {
      const isNo = userOption.user_story_paths.find((x) =>
        x.code.includes("-NO")
      );
      if (isNo) {
        setIsOkButton(true);
        setIsGoButton(false);
      }
    }
  };

  const handleIsOk = () => {
    handleUserStoryChange(who);
  };

  const header = (
    <>
      <h3>
        Hi{userName ? " " : ""}
        {userName}, welcome to our Community Information Tool
      </h3>
      <p>
        The Community Information Tool offers insight into communities across
        B.C. with integrated socio-economic data, infrastructure, and community
        assets data. The Tool supports community, regional, and province-wide
        planning, which is essential to building thriving, healthy communities.
      </p>
    </>
  );

  const resetButton = (
    <Button
      variant="outline-primary"
      className="user-story-button"
      onClick={resetUserStory}
    >
      Reset Search Criteria
    </Button>
  );

  const okButton = (
    <Button
      variant="outline-primary"
      className="user-story-button"
      onClick={handleIsOk}
      active
    >
      Ok
    </Button>
  );

  const goButton = (
    <Button
      variant="primary"
      active
      className="user-story-button"
      onClick={() => showResult(redirectUrl)}
    >
      Let&apos;s Go <ArrowRight />
    </Button>
  );

  return (
    <>
      <div className="my-4 top-container">
        <div className={showReport ? "x-smaller-section-border" : ""}>
          <div className={showReport ? "x-smaller-section" : ""}>
            {showUserStoryText && <Row>{header}</Row>}
            <Row>
              <Col sm={9}>
                <Row>
                  {userOptions.map((story) => (
                    <>
                      {showUserStoryText && story.preTextLabel && (
                        <>{ReactHtmlParser(story.preTextLabel)}</>
                      )}
                      <UserStoryItem
                        key={story.id}
                        userStory={story}
                        onUserStoryChange={handleUserStoryChange}
                      />
                    </>
                  ))}
                </Row>
                {isGoButton && (
                  <Row className="section-break">
                    {resetButton} {goButton}
                  </Row>
                )}
                {isOkButton && <Row className="section-break">{okButton}</Row>}
              </Col>
              {showUserStoryText && (
                <Col sm={3} className="svg-box pt-3 user-story-image">
                  <img
                    className="add-opp-img"
                    src="/images/CIT_logo.svg"
                    height="100%"
                    width="100%"
                    alt="cit logo mountains"
                  />
                </Col>
              )}
            </Row>
          </div>
        </div>
        {showReport && (
          <>
            <div className="report-section">
              {powerBiReport.includes("overview") && <ReportOverview />}
              {powerBiReport.includes("compare") && <ReportCompare />}
              {powerBiReport.includes("criteriaSearch") && (
                <ReportCriteriaSearch />
              )}
            </div>
          </>
        )}
      </div>
    </>
  );
}
