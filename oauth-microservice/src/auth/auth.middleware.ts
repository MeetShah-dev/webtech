import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

@Injectable()
export class AuthMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    const excludedRoutes = ['/auth/google/login', '/auth/google/redirect/*', '/auth/status']; // Add routes that should be excluded from authentication
    if (excludedRoutes.includes(req.originalUrl)) {
      // Skip authentication for excluded routes
      return next();
    }
    // Check if user is authenticated
    if (req.isAuthenticated()) {
      // If authenticated, set user information in request object
      req.user = req.user; // You can access user info from req.user after authentication
      next();
    } else {
      // If not authenticated, handle it accordingly
      res.status(401).send('Unauthorized'); // Or redirect to login page, etc.
    }
  }
}
