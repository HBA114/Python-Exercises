import React, { useEffect, useState } from "react"

export default function Post() {
    const [posts, setPosts] = useState([])

    useEffect(() => {
        const fetchPosts = async () => {
            const response = await fetch(
                "http://localhost:8000/posts/",
                {
                    headers: { 'Content-Type': 'application/json' }
                }
            )
            const content = await response.json()
            console.log(content)
            setPosts(content)
        }

        fetchPosts()
    },[])

    return (<div>
        <h1>Posts</h1>
    </div>)
}