import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';
import { Reflector } from '@nestjs/core';
import { ROLES_KEY } from '../decorators/roles.decorator';
import { Role } from '../enums/role.enum';

@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const requiredRoles = this.reflector.getAllAndOverride<Role[]>(ROLES_KEY, [
      context.getHandler(),
      context.getClass(),
    ]);
    if (!requiredRoles) {
      return true;
    }
    const { user } = context.switchToHttp().getRequest();
    return requiredRoles.some((role) => {
      switch (role) {
        case Role.ADMIN:
          // Admin has rights of Moderator and User
          return user.role_id === Role.ADMIN || user.role_id === Role.MODERATOR || user.role_id === Role.USER;
        case Role.MODERATOR:
          // Moderator has rights of User
          return user.role_id === Role.MODERATOR || user.role_id === Role.USER;
        case Role.USER:
          // User has only rights of User
          return user.role_id === Role.USER;
        default:
          return false; // Unknown role, deny access
      }
    });
  }
}