
import React from 'react'
import SkillsList from './SkillsList'

const Skills = () => {

    const frontend = ['JavaScript','React/Redux','HTML','CSS','Bootstrap','SemanticUI']
    const backend = ['Python', 'Django', 'AWS', 'PostgreSQL']
    const gameDev = ['Unity','Phaser','PyGame']

    return (
        <>
            <h1 className="ui center aligned basic segment">Skills</h1>
            <div className="ui centered raised cards">
                <div className="card">
                    <div className="content">
                        <div className="center aligned header">
                            Frontend Tech Stack
                        </div>
                        <div className="center aligned">
                            <SkillsList skills = {frontend}/>
                        </div>
                    </div>
                </div>
                <div className="card">
                    <div className="content">
                        <div className="center aligned header">
                            Backend Tech Stack
                        </div>
                        <div className="center aligned">
                            <SkillsList skills = {backend}/>
                        </div>
                    </div>
                </div>
                <div className="card">
                    <div className="content">
                        <div className="center aligned header">
                            Game Development
                        </div>
                        <div className="center aligned">
                            <SkillsList skills = {gameDev}/>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Skills;
