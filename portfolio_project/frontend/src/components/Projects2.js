import React, {useState,useEffect} from 'react'
import ProjectCard from './ProjectCard'
import projects from '../apis/projects'

const Projects = () => {
    const [projectInfo,setProjectInfo] = useState([]);

    const fetchProjects  = async () =>{
        const response = await projects.get('/projects/')
        setProjectInfo(response.data)
    }

    useEffect(()=>{
        fetchProjects()
    },[])

    return (
        <>
            <div className="ui center aligned container">
                <h1>Projects</h1>
                <h2>{projectInfo.length}</h2>
                {console.log(projectInfo)}
            </div>
            <div className="ui three raised cards">
                <ProjectCard /> 
                <ProjectCard />
                <ProjectCard />
                <ProjectCard />
                <ProjectCard />
                <ProjectCard /> 
            </div>
        </>
    )
}

export default Projects;