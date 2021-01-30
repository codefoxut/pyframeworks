import React from 'react'

const ProjectCard = () => {
    return (
        <div className="card"> 
            <div className= "image">
                <img></img>
            </div>
            <div className="content">
                <div className="header">
                    Project Name Here
                </div>
                <div className="description">
                    <p>Project description goes here.</p>
                </div>
            </div>
            <div className="extra content">
                <button className="ui button">
                    Code
                </button>
                <button className="ui button">
                    Demo
                </button>
            </div>
        </div>
    )
}

export default ProjectCard;