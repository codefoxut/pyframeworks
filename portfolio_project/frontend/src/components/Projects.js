
import ProjectCard from './ProjectCard'

const Projects = () => {
    return (
        <>
            <h2>Project Component</h2>
            <div className="ui three cards">
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