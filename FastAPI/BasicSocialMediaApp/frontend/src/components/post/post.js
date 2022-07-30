import React, { useEffect, useState } from "react"
import data from '../../myData.json';

const getPostsRequestAddress = data["get_posts"];

export default function Post() {
    const [posts, setPosts] = useState([])

    useEffect(() => {
        const fetchPosts = async () => {
            const response = await fetch(
                getPostsRequestAddress,
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