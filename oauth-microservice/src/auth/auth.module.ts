import { Module } from '@nestjs/common';
import { UserService } from './user/user.service';
import { AuthController } from './auth/auth.controller';
import { Oauth } from './oauth/oauth';
import { Jwt } from './jwt/jwt';

@Module({
  providers: [UserService, Oauth, Jwt],
  controllers: [AuthController]
})
export class AuthModule {}
