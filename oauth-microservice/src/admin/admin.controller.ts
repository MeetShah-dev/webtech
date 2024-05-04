import { HttpService } from '@nestjs/axios';
import { Controller, Delete, Get, Post, Put, Req, Res } from '@nestjs/common';
import { AdminService } from './admin.service';
import { Roles } from 'src/decorators/roles.decorator';
import { Role } from 'src/enums/role.enum';

@Controller('admin')
export class AdminController {
    constructor(
        private readonly adminService: AdminService
    ) { }
    @Roles(Role.MODERATOR)
    @Post('add-category')
    addCategory(@Req() req, @Res() res: Response) {
        return this.adminService.addCategory(req, res)
    }
    @Roles(Role.MODERATOR)
    @Put('approve-post')
    approvePost(@Req() req, @Res() res: Response) {
        return this.adminService.approvePost(req, res)
    }
    @Roles(Role.MODERATOR)
    @Post('add-categories')
    addCategories(@Req() req, @Res() res: Response) {
        return this.adminService.addCategories(req, res)
    } 
    @Roles(Role.MODERATOR)
    @Put('reject-post')
    rejectPost(@Req() req, @Res() res: Response) {
        return this.adminService.rejectPost(req, res)
    }
    @Roles(Role.MODERATOR)
    @Post('post-feedback')
    postFeedback(@Req() req, @Res() res: Response) {
        return this.adminService.postFeedback(req, res)
    } 
    @Roles(Role.MODERATOR)
    @Delete('delete-comment')
    deleteComment(@Req() req, @Res() res: Response) {
        return this.adminService.deleteComment(req, res)
    }
    @Roles(Role.USER)
    @Post('add-category-blog')
    addCategoryBlog(@Req() req, @Res() res: Response) {
        return this.adminService.addCategoryBlog(req, res)
    }
    @Roles(Role.USER)
    @Get('all-categories')
    getAllCategories(@Req() req, @Res() res: Response) {
        return this.adminService.getAllCategories(req, res)
    }
    @Roles(Role.ADMIN)
    @Get('all-users')
    getAllUsers(@Req() req, @Res() res: Response) {
        return this.adminService.getAllUsers(req, res)
    }
    @Roles(Role.ADMIN)
    @Put('change-role')
    changeRole(@Req() req, @Res() res: Response) {
        return this.adminService.changeRole(req, res)
    }
    @Roles(Role.MODERATOR)
    @Get('get-ready-posts')
    getReadyPosts(@Req() req, @Res() res: Response) {
        return this.adminService.getReadyPosts(req, res)
    }
    @Roles(Role.USER)
    @Get('get-all-magazines')
    getAllMagazines(@Req() req, @Res() res: Response) {
        return this.adminService.getAllMagazines(req, res)
    }
}


