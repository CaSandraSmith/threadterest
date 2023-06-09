import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import { createBoardThunk } from "../../store/boards";
import ChangeBoardCoverModal from "../UpdateBoardModal/ChangeBoardCoverModal";
import { fetchPinsToday } from "../../store/pins";
import SavePinsToBoardModal from "./SavePinsToBoard";
import './CreateBoardModal.css'




function CreateBoardModal({ username }) {

  const dispatch = useDispatch();
  const history = useHistory()
  const [name, setName] = useState("");
  const [isPrivate, setIsPrivate] = useState(false);
  const [errors, setErrors] = useState([]);
  const [description,setDescription] = useState("")
  const { setModalContent, closeModal } = useModal();

  console.log("USER NAME", username)

  const stateCheck = useSelector((state) => state)
  console.log("STATE CHECK FOR BOARD", stateCheck)


  useEffect(() => {
  }, [name, isPrivate])

  let pinsTodayObj = useSelector(state => state.pins.todayPins)
  let testUsername = useSelector(state => state.session.user)
  console.log("THIS IS THE USER FOR CREATE BOARD", testUsername)





  let pinsToday
  if (pinsTodayObj) {
    pinsToday = shuffle(Object.values(pinsTodayObj))
    // dbLatestDate = pinsToday[0].created_at
  }
  const date = new Date();

  console.log("PINS TODAY CREATE BOARD MODAL", pinsToday)
  useEffect(() => {
    dispatch(fetchPinsToday())
  }, [])

  const month = date.toLocaleString('default', { month: 'long' });
  let year = date.getFullYear();
  let day = date.getDate();




  const disabledButton = name === "";

  const handlePrivateChange = (e) => {
    setIsPrivate(e.target.checked);
  };


  const onSubmit = async (e) => {
    e.preventDefault(); // Prevent the default form submission


    //VALIDATIONS



    //create form data
    const formData = {
      name,
      private: isPrivate,
      description: description
    }
    //log formData
    console.log("FORM DATA:", formData)
    await dispatch(createBoardThunk(formData))
    history.push(`/${username}/${formData.name}`)
    closeModal()
    openModal()

    // openModal(<SavePinsToBoardModal />);

    // history.push('/boards/1')
  };

  const openModal = () => {
    const modalContent = (
      <div>
        <SavePinsToBoardModal pinsToday={pinsToday} username={username} boardName={name} />
      </div>
    );
    setModalContent(modalContent);
  };

  function shuffle(array) {
    let currentIndex = array.length, randomIndex;

    while (currentIndex != 0) {

      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;

      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }

    return array;
  }


  return (
    <>
      <div className="create-board-modal-container">

        <div className="create-board-modal-header">
          Create board
        </div>

        <form onSubmit={onSubmit}>

          <label className="create-board-modal-name">
            Name
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
              className="create-board-modal-name-input"

            ></input>
          </label>

          <label>
            <div className="create-board-modal-flex-row">

              <input type="checkbox" checked={isPrivate} onChange={handlePrivateChange} className="checkbox-input" />

              <div>
                <p className="create-board-modal-private-text bold">Keep this board secret</p>
                <p className="create-board-modal-private-text">So only you and collaborators can see it. Learn more</p>
              </div>

            </div>
          </label>

          {/* <button type="submit" className="create-board-modal-create-button" disabled={disabledButton} onClick={openModal}> */}
          <button type="submit" className="create-board-modal-create-button" disabled={disabledButton}>
            Create
          </button>

        </form>
      </div>
    </>
  )

}


export default CreateBoardModal
