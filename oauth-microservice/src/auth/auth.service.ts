import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from '../user/entities/user.entity';
import { Repository } from 'typeorm';

@Injectable()
export class AuthService {
  constructor(
    @InjectRepository(User) private readonly userRepo: Repository<User>,
  ) { }

  async validateUser(email: string, name: any, photo: any) {
    const user = await this.userRepo.findOne({ where: { email: email } });
    if (user) {
      return user;
    }
    const newUser = this.userRepo.create({ email, first_name: name.givenName, last_name: name.familyName, profile_photo: photo[0].value, role_id: 3 });
    await this.userRepo.save(newUser)
    return newUser;
  }

  async findUser(id: string) {
    const user = await this.userRepo.findOne({ where: { id } });
    return user;
  }

  handlerLogin() {
    return 'handlerLogin';
  }

  handlerRedirect() {
    return 'handlerRedirect';
  }
}
