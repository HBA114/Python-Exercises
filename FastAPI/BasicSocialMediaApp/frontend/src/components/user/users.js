import React, { useEffect, useState } from "react"
import data from "../../myData.json"

const userRequestAddress = data["get_users"]

export default function Users() {
    const [users, setUsers] = useState([])

    useEffect(() => {
        const fetchUsers = async () => {
            const response = await fetch(
                userRequestAddress,
                {
                    headers: { 'Content-Type': 'application/json' }
                }
            )
            const content = await response.json()
            setUsers(content)
        }
        fetchUsers()
    }, [])

    const handleClick = (user) =>{
        console.log(user)
    }

    const userCard = (user) => {
        return (
            <div onClick={() => handleClick(user)} className="card" style={{ width: "200px", margin: "20px" }}>
                <div>
                    <img style={{ padding: "5px" }} height="200px" alt="img" className="card-img-top rounded-circle" src={user.photo_base64} />
                </div>
                <div className="card-body">
                    <h6>{"Email : "+user.email}</h6>
                </div>
            </div>
        )
    }

    return (
        <div>
            <table>
                <tbody>
                    {
                        [...Array(Math.ceil(users.length / 3))].map((element, index) =>
                            <tr key={index}>
                                <td>{userCard(users[index])}</td>
                                <td>{users[3 * index + 1] ? userCard(users[3 * index + 1]) : null}</td>
                                <td>{users[3 * index + 2] ? userCard(users[3 * index + 2]) : null}</td>
                            </tr>
                        )
                    }
                </tbody>
            </table>
        </div>
    )
}