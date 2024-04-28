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

    // Define the role values with hierarchical access rights
    const userRoleValue = this.getRoleValue(user.role_id);
    return requiredRoles.some(role => userRoleValue >= this.getRoleValue(role));
  }

  private getRoleValue(role: Role): number {
    // Higher number implies higher privileges
    switch (role) {
      case Role.ADMIN:
        return 3;
      case Role.MODERATOR:
        return 2;
      case Role.USER:
        return 1;
      default:
        return 0; // Undefined roles get the lowest priority
    }
  }
}
