import { Controller, Delete, Get, Post, Put, Req, Res, UploadedFiles, UseInterceptors } from '@nestjs/common';
import { BlogService } from './blog.service';
import { Roles } from '../decorators/roles.decorator';
import { Role } from '../enums/role.enum';
import { AnyFilesInterceptor } from '@nestjs/platform-express';


@Controller('blog')
export class BlogController {
    constructor(private readonly blogService: BlogService) { }
    @Roles(Role.USER)
    @Get('magazine-feed')
    magazineFeed(@Req() req, @Res() res: Response) {
        return this.blogService.getLatestMagazine(req, res)
    }
    @Roles(Role.USER)
    @Get('archived-magazine')
    archived(@Req() req, @Res() res: Response) {
        return this.blogService.getArchiveMagazine(req, res)
    }

    @Roles(Role.USER)
    @UseInterceptors(AnyFilesInterceptor())
    @Post('create-blog')
    createBlog(@UploadedFiles() files: Array<Express.Multer.File>, @Req() req, @Res() res: Response) {
        return this.blogService.createBlog(req, res, files)
    }

    @Roles(Role.USER)
    @Get('read-user-blogs')
    readUserBlog(@Req() req, @Res() res: Response) {
        return this.blogService.getUserReadBlog(req, res)
    }

    @Roles(Role.USER)
    @Get('read-drafts')
    userDrafts(@Req() req, @Res() res: Response) {
        return this.blogService.getUserDrafts(req, res)
    }

    @Roles(Role.USER)
    @Get('read-blog')
    readBlog(@Req() req, @Res() res: Response) {
        return this.blogService.getReadBlog(req, res)
    }

    @Roles(Role.USER)
    @UseInterceptors(AnyFilesInterceptor())
    @Put('update-blog')
    updateBlog(@UploadedFiles() files: Array<Express.Multer.File>, @Req() req, @Res() res: Response) {
        return this.blogService.updateBlog(req, res, files)
    }

    @Roles(Role.USER)
    @Delete('delete-blog')
    deleteBlog(@Req() req, @Res() res: Response) {
        return this.blogService.deleteBlog(req, res)
    }

    @Roles(Role.USER)
    @Delete('delete-file')
    deleteFile(@Req() req, @Res() res: Response) {
        return this.blogService.deleteFile(req, res)
    }

    @Roles(Role.USER)
    @Get('read-user-rejected-blogs')
    readUserRejectedBlogs(@Req() req, @Res() res: Response) {
        return this.blogService.getReadUserRejectedBlogs(req, res)
    }

    @Roles(Role.USER)
    @Post('add-reader')
    addReader(@Req() req, @Res() res: Response) {
        return this.blogService.addReader(req, res)
    }

    @Roles(Role.USER)
    @Get('user-notifications')
    getUserNotifications(@Req() req, @Res() res: Response) {
        return this.blogService.getUserNotifications(req, res)
    }
   
}

