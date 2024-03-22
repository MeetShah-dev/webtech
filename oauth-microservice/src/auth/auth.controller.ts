import { Controller, Get, UseGuards, Req, Redirect } from '@nestjs/common';
import { AuthService } from './auth.service';
import { GoogleGuard } from '../guards/google.guard';
import { Request } from 'express';

@Controller('auth')
export class AuthController {

  constructor(private readonly authService: AuthService) { }

  @UseGuards(GoogleGuard)
  @Get('google/login')
  handlerLogin() {
    return this.authService.handlerLogin()
  }

  @UseGuards(GoogleGuard)
  @Get('google/redirect')
  redirect() {
    return this.authService.handlerRedirect()
  }

  @Get('status')
  user(@Req() req: Request) {
    if (req.user) {
      return { message: 'Authenticated', user: req.user }
    } else {
      return { message: 'Not Authenticated' }
    }
  }
}