import { Inject, Injectable } from '@nestjs/common';
import { PassportSerializer } from '@nestjs/passport';
import { AuthService } from './auth.service';
import { User } from '../user/entities/user.entity';

@Injectable()
export class SessionSerializer extends PassportSerializer {
  constructor(
    @Inject('AUTH_SERVICE') private readonly authService: AuthService,
  ) {
    super();
  }

  serializeUser(user: User, done: Function) {
    done(null, user);
  }
  async deserializeUser(payload: any, done: Function) {
    console.log('payload', payload)
    const user = await this.authService.findUser(payload.id);
    if (user) {
      return done(null, user)
    }
    return done(null, null);
  }
}