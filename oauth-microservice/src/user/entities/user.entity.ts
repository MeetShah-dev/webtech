import { Column, Entity, PrimaryGeneratedColumn, Unique } from "typeorm";

@Entity('user')
@Unique(['email'])
export class User {
    @PrimaryGeneratedColumn()
    id: string
    
    @Column({nullable: true})
    last_login_date: Date

    @Column()
    first_name: string

    @Column()
    last_name: string

    @Column()
    email: string

    @Column({nullable: true})
    date_of_birth: string
    

    @Column({nullable: true})
    date_created: Date

    @Column({nullable: true})
    date_updated: Date

    @Column({nullable: true})
    email_notification: string

    @Column({nullable: true})
    profile_photo: string

    @Column({nullable: true})
    nationality: string

    @Column({nullable: true})
    type: string

    @Column({nullable: true})
    gender: string

    @Column({nullable: true})
    banned: boolean

    @Column({nullable: true})
    role_id: number
}