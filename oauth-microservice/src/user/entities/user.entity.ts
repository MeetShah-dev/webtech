import { Column, Entity, PrimaryGeneratedColumn, Unique } from "typeorm";

@Entity('user')
@Unique(['email'])
export class User {
    @PrimaryGeneratedColumn('uuid')
    id: string
    
    @Column()
    password: string

    @Column()
    last_login: Date

    @Column()
    first_name: string

    @Column()
    last_name: string

    @Column()
    email: string

    @Column()
    date_of_birth: string

    @Column()
    date_created: Date

    @Column()
    date_updated: Date

    @Column()
    email_notification: string

    @Column()
    profile_photo: string

    @Column()
    nationality: string

    @Column()
    type: string

    @Column()
    gender: string

    @Column()
    role_id: number
}