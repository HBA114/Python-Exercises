import { useEffect, useState } from 'react';
import './App.css';
import Post from './components/post/post';
import CreateUser from './components/user/create_user';
import Users from './components/user/users';


function App() {

  const [users, setUsers] = useState([])

  useEffect(()=>{
    const fetchUsers = async () =>{
      const response = await fetch(
        "http://localhost:8000/users/",
        {
          headers: {'Content-Type': 'application/json'}
        }
      )
      const content = await response.json()
      console.log(content)
    }

    fetchUsers()
  }, [])


  return (
    <div>
        <Users />
    </div>
  );
}

export default App;
