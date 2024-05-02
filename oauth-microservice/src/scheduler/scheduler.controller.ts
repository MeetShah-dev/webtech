import { Controller, Delete, Get, Post, Req, Res } from '@nestjs/common';
import { Roles } from 'src/decorators/roles.decorator';
import { Role } from 'src/enums/role.enum';
import { SchedulerService } from './scheduler.service';

@Controller('scheduler')
export class SchedulerController {
    constructor(private readonly schedulerService: SchedulerService) {}
    @Roles(Role.USER)
    @Get('get-all-user-likes')
    getAllUserLikes(@Req() req, @Res() res: Response) {
        return this.schedulerService.getAllUserLikes(req, res)
    }
    @Get('get-all-user-dislikes')
    getAllUserDislikes(@Req() req, @Res() res: Response) {
        return this.schedulerService.getAllUserDislikes(req, res)
    }
    @Get('get-all-comments')
    getAllComments(@Req() req, @Res() res: Response) {
        return this.schedulerService.getAllComments(req, res)
    }
    @Post('add-comment')
    addComment(@Req() req, @Res() res: Response) {
        return this.schedulerService.addComment(req, res)
    }
    @Post('edit-comment')
    editComment(@Req() req, @Res() res: Response) {
        return this.schedulerService.editComment(req, res)
    }
    @Post('update-like-dislike')
    updateLikeDislike(@Req() req, @Res() res: Response) {
        return this.schedulerService.updateLikeDislike(req, res)
    }
    @Roles(Role.USER)
    @Post('create-schedule')
    createScheduler(@Req() req, @Res() res: Response) {
        return this.schedulerService.createSchedule(req, res)
    }
    @Roles(Role.USER)
    @Post('re-schedule')
    reScheduler(@Req() req, @Res() res: Response) {
        return this.schedulerService.reSchedule(req, res)
    }
    @Get('get-all-magazine')
    getAllMagazines(@Req() req, @Res() res: Response) {
        return this.schedulerService.getAllMagazine(req, res)
    }
    @Post('delete-comment')
    deleteComment(@Req() req, @Res() res: Response) {
        return this.schedulerService.deleteComment(req, res)
    }
}
