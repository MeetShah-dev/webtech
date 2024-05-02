import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from '../user/entities/user.entity';
import { Repository } from 'typeorm';
import { HttpService } from '@nestjs/axios';
import { firstValueFrom } from 'rxjs';
const IRMAK_API = 'http://3.89.135.95:8000/'
const BLOGGING_API = 'http://54.82.93.84:8000/api/'
@Injectable()
export class AuthService {
  constructor(
    @InjectRepository(User) private readonly userRepo: Repository<User>,
    private httpService: HttpService
  ) { }

  async validateUser(email: string, name: any, photo: any) {
    const users = await this.userRepo.findAndCount()
    const user = await this.userRepo.findOne({ where: { email: email } });
    console.log('the user--', users)
    if (user) {
      return user;
    }
    const newUser = this.userRepo.create({ email, first_name: name.givenName, last_name: name.familyName, profile_photo: photo[0].value, role_id: 1 });
    await this.userRepo.save(newUser)
    return newUser;
  }

  async findUser(id: string) {
    const user = await this.userRepo.findOne({ where: { id } });
    return user;
  }
  async findByEmail(email: string) {
    const user = await this.userRepo.findOne({ where: { email } });
    return user;
  }
  async allUsers() {
    const users = await this.userRepo.find();
    return users;
  }

  handlerLogin() {
    return 'handlerLogin';
  }

  async addCategory(req, res) {
    let payload = req.body;
    try {
      const response = await firstValueFrom(this.httpService.post(IRMAK_API + 'addCategory', payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      }));
      return res.json(response.data);
    } catch (e) {
      console.log("error", e)
    }
  }

  async approvePost(req, res) {
    let payload = req.body;
    try {
      const response = await firstValueFrom(this.httpService.put(IRMAK_API + 'approvePost', payload, {
        headers: {
          'Content-Type': 'application/json'
        }
      }));
      return res.json(response.data);
    } catch (e) {
      console.log("error", e)
    }
  }

  handlerRedirect() {
    return 'handlerRedirect';
  }
}
