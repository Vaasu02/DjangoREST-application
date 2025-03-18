import { useState, useEffect } from "react";
import api from "../api";
import Note from "../components/Note";
import '../styles/Home.css';

const Home = () => {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  useEffect(() => {
    getNotes();
  }, []);

  const getNotes = () => {
    api
      .get("/api/notes/")
      .then((res) => res.data)
      .then((data) => {
        setNotes(data), console.log(data);
      })
      .catch((error) => alert(error));
  };

  const deleteNotes = async (id) => {
    await api
      .delete(`/api/notes/delete/${id}/`)
      .then((res) => {
        if (res.status === 204) {
          alert("Note deleted successfully");
        } else {
          alert("Error deleting note");
        }
        getNotes();
      })
      .catch((err) => {
        alert(err);
      });
  };

  const creatNotes = async (e) => {
    e.preventDefault();
    await api
      .post("/api/notes/", { title, content })
      .then((res) => {
        if (res.status === 201) {
          alert("Note created successfully");
          setTitle("");
          setContent("");
          getNotes();
        } else {
          alert("Error creating note");
        }
      })
      .catch((err) => {
        alert(err);
      });
  };

  return(
    <div>
      <div>
        <h2>Notes</h2>
        {notes.map((note) => (
          <Note key={note.id} note={note} onDelete={deleteNotes} />
        ))}
      </div>
      <h2>Create a Note</h2>
      <form onSubmit={creatNotes}>
        <label htmlFor="title">Title : </label>
        <br />
        <input
          type="text"
          id="title"
          required
          name="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <br />
        <label htmlFor="content">Content : </label>
        <br />
        <textarea
          id="content"
          required
          name="content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <br />
        <input type="submit" value="Submit"></input>
      </form>
    </div>
  );
};

export default Home;
