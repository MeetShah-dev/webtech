import { Inject, Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';
import axios from 'axios';
import { AuthService } from './auth.service';

@Injectable()
export class AuthMiddleware implements NestMiddleware {
  constructor(@Inject('AUTH_SERVICE') private readonly authService: AuthService) {}
  async use(req: Request, res: Response, next: NextFunction) {
    const excludedRoutes = ['/auth/google/login', '/auth/google/redirect/*', '/auth/status'];
    if (excludedRoutes.some(route => req.originalUrl.startsWith(route))) {
      return next();
    }

    if (req.isAuthenticated()) {
      next();
    } else {
      const authToken = req.headers.authorization;
      if (!authToken || !authToken.startsWith('Bearer ')) {
        return res.status(401).send('Unauthorized: No token provided');
      }

      const token = authToken.slice(7); // Remove 'Bearer ' from the start
      try {
        // Validate the access token with Google's tokeninfo endpoint
        const response = await axios.get(`https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=${token}`);
        if (response.data && response.data.user_id) {
          // Assuming the response includes a user_id which indicates a valid token
          req.user = await this.authService.findByEmail(response.data.email);
          req['isAuthenticated'] = () => true; // Mimic isAuthenticated method
          console.log("USER---",req.user, response.data)
          next();
        } else {
          throw new Error('Invalid token: Google API did not return user_id');
        }
      } catch (error) {
        console.error('Token validation error:', error);
        return res.status(401).send('Unauthorized: Invalid token');
      }
    }
  }
}
