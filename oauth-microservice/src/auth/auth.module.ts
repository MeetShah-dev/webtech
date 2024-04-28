import { Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { AuthController } from './auth.controller';
import { ConfigModule } from '@nestjs/config';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from '../user/entities/user.entity';
import { GoogleStrategy } from './google.strategy';
import { SessionSerializer } from './session.serializer';
import { PassportModule } from '@nestjs/passport';
import { HttpModule } from '@nestjs/axios';
import { AuthMiddleware } from './auth.middleware';

@Module({
  imports: [
    PassportModule.register({ session: true }),
    ConfigModule.forRoot({
      isGlobal: true,
      envFilePath: '.env',
    }),
    HttpModule,
    TypeOrmModule.forFeature([User]),
  ],
  controllers: [AuthController],
  providers: [
    AuthService, 
    GoogleStrategy, 
    SessionSerializer,
    {
      provide: 'AUTH_SERVICE',
      useClass: AuthService
    }
  ],
  exports: [AuthService, 'AUTH_SERVICE']  // Make sure to export AuthService and the custom provider
})
export class AuthModule { }
