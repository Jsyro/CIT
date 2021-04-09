import { useState } from "react";
import PropTypes from "prop-types";
import "./NumberRangeFilter.scss";
import { Button } from "shared-components";
import { Modal } from "react-bootstrap";
import "react-input-range/src/scss/index.scss";
import InputRangeWithTextboxes from "../InputRangeWithTextboxes/InputRangeWithTextboxes";

export default function NumberRangeFilter(props) {
  const {
    inputRange,
    units,
    description,
    label,
    isDistance,
    isSelected,
    setIsSelected,
    inputRangeValue,
    setInputRangeValue,
    initialInputRangeValues,
    displayRange,
    setDisplayRange,
  } = props;
  const [show, setShow] = useState(false);
  const [minInput, setMinInput] = useState(inputRange.min);
  const [maxInput, setMaxInput] = useState(inputRange.max);
  const [validMax, setValidMax] = useState(true);
  const [validMin, setValidMin] = useState(true);
  const [isModified, setIsModified] = useState(false);

  const inputRangeMax = initialInputRangeValues.max;
  const inputRangeMin = initialInputRangeValues.min;

  const handleSave = () => {
    setIsSelected(isModified);
    setShow(false);
    setDisplayRange({
      min: inputRangeValue.min,
      max: inputRangeValue.max,
    });
  };
  const handleClear = () => {
    setInputRangeValue({ min: inputRangeMin, max: inputRangeMax });
    setMaxInput(inputRangeMax);
    setMinInput(inputRangeMin);
    setValidMin(true);
    setValidMax(true);
    setIsModified(false);
  };
  const handleShow = () => setShow(true);
  const handleClose = () => {
    setShow(false);
    // Reset values to previous state
    setInputRangeValue({ ...displayRange });
    setMaxInput(displayRange.max);
    setMinInput(displayRange.min);
    setValidMin(true);
    setValidMax(true);
  };

  const handleModified = (value, setStateFunction) => {
    setIsModified(true);
    setStateFunction(value);
  };

  return (
    <>
      {!isSelected ? (
        <Button
          label={label}
          styling="bcgov-normal-white filter-button unselected btn"
          onClick={handleShow}
        />
      ) : (
        <Button
          label={`${label}: ${isDistance ? "within" : ""} ${displayRange.min}-${
            displayRange.max
          } ${units}`}
          styling="bcgov-normal-blue filter-button selected btn"
          onClick={handleShow}
        />
      )}

      <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
      >
        <Modal.Header closeButton>
          <Modal.Title>{label}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>{description}</p>
          <InputRangeWithTextboxes
            inputRange={inputRange}
            units={units}
            minInput={minInput}
            setMinInput={(value) => handleModified(value, setMinInput)}
            maxInput={maxInput}
            setMaxInput={(value) => handleModified(value, setMaxInput)}
            inputRangeValue={inputRangeValue}
            setInputRangeValue={(value) =>
              handleModified(value, setInputRangeValue)
            }
            validMax={validMax}
            validMin={validMin}
            setValidMax={setValidMax}
            setValidMin={setValidMin}
          />
        </Modal.Body>
        <Modal.Footer>
          <Button
            label="Reset"
            styling="bcgov-normal-white mr-auto modal-reset-button btn"
            onClick={handleClear}
          />
          <Button
            label="Save"
            styling="bcgov-normal-blue modal-save-button btn"
            onClick={handleSave}
            disabled={!validMin || !validMax}
          />
        </Modal.Footer>
      </Modal>
    </>
  );
}

NumberRangeFilter.defaultProps = {
  isDistance: false,
};

NumberRangeFilter.propTypes = {
  inputRange: PropTypes.shape({
    min: PropTypes.number.isRequired,
    max: PropTypes.number.isRequired,
  }).isRequired,
  units: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  isDistance: PropTypes.bool,
  isSelected: PropTypes.bool.isRequired,
  setIsSelected: PropTypes.func.isRequired,
  inputRangeValue: PropTypes.shape({
    max: PropTypes.number.isRequired,
    min: PropTypes.number.isRequired,
  }).isRequired,
  setInputRangeValue: PropTypes.func.isRequired,
  initialInputRangeValues: PropTypes.shape({
    max: PropTypes.number.isRequired,
    min: PropTypes.number.isRequired,
  }).isRequired,
  displayRange: PropTypes.shape({
    max: PropTypes.number.isRequired,
    min: PropTypes.number.isRequired,
  }).isRequired,
  setDisplayRange: PropTypes.func.isRequired,
};
