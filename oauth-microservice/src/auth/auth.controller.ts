import { Controller, Get, UseGuards, Req, Redirect, Res, Post, Put } from '@nestjs/common';
import { AuthService } from './auth.service';
import { GoogleGuard } from '../guards/google.guard';
import { Request, Response } from 'express';
import { Roles } from '../decorators/roles.decorator';
import { Role } from '../enums/role.enum';

@Controller('auth')
export class AuthController {

  constructor(private readonly authService: AuthService) { }

  @UseGuards(GoogleGuard)
  @Get('google/login')
  handlerLogin() {
    return this.authService.handlerLogin()
  }

  @Post('addCategory')
  forwardPostApi(@Req() req, @Res() res: Response) {
    return this.authService.addCategory(req, res)
  }

  @Put('approvePost')
  approvePost(@Req() req, @Res() res: Response) {
    return this.authService.approvePost(req, res)
  }

  @Get('google/redirect')
  @UseGuards(GoogleGuard)
  async googleLoginRedirect(@Req() req, @Res() res: Response) {
    // After successful authentication, this route will be called with the user data in req.user
    const user = req.user;
    const token = user.accessToken;  // Assuming the token is needed on the client-side
    const userData = encodeURIComponent(JSON.stringify(user));

    // Redirect to the Vue.js frontend with the user data as a query parameter
    res.redirect(`http://localhost:5174/dashboard?user=${userData}&token=${token}`);
  }
  @Get('all-users')
  allUsers(@Req() req, @Res() res: Response) {
    return this.authService.allUsers()
  }
  @Get('status')
  @Roles(Role.MODERATOR)
  user(@Req() req: Request) {
    if (req.user) {
      return { message: 'Authenticated', user: req.user }
    } else {
      return { message: 'Not Authenticated' }
    }
  }
}